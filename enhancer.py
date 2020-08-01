from PIL import Image, ImageEnhance

im = Image.open("sample.jpg")   # Image file
enhancer = ImageEnhance.Sharpness(im)
enhanced_im = enhancer.enhance(7.0)
enhanced_im.save("new_sample.jpg")  # enhanced Image file


