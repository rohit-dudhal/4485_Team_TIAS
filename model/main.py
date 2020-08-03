
from flask import Flask, render_template, Response
from camera import VideoCamera
from mail_sending import Mail_sending
ln=['Tejas','Rohit']
c=0

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:        
        frame = camera.get_frame()
        # name=camera.get_name()
        # if(name in ln):
        #     b=Mail_sending().send_mail(name)
        #     ln.remove(name)
        yield (b'--frame\r\n' 
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
    