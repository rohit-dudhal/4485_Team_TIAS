from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GT', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    #base64 to cv2
    encoded_data = image_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('image.jpg', img)

    # enhancing image
    im = Image.open('image.jpg')
    enhancers = ImageEnhance.Sharpness(im)
    enhanced_im = enhancers.enhance(2.75)
    enhanced_im.save("sample.jpg")

    im = Image.open('sample.jpg')
    enhancercon = ImageEnhance.Contrast(im)
    enhanced_im = enhancercon.enhance(1.2)
    enhanced_im.save("sample.jpg")

    im = Image.open('sample.jpg')
    enhancerc = ImageEnhance.Color(im)
    enhanced_im = enhancerc.enhance(1.1)
    enhanced_im.save("sample.jpg")
    # enhanced Image file

    data = {}
    with open('sample.jpg', mode='rb') as file:
        imgw = file.read()
    data['imgw'] = base64.b64encode(imgw)


    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    response = jsonify(util.classify_image("b," + str(data['imgw'])[2:]))
  

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
