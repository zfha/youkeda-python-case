from PIL import Image
origin = Image.open('1.jpg')
hat = Image.open('christmas_hat.png')
resizeHat= hat.resize((300, 300))
origin.paste(resizeHat, (100, 100, 400, 400), resizeHat)
origin.save('merge.jpg')