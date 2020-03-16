from PIL import Image
im = Image.open('christmas_hat.png')
width, height = im.size
resizeImg = im.resize((width / 2, height / 2))
resizeImg.save("thumbnail.png")