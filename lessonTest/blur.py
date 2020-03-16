
from PIL import Image, ImageFilter

# 打开一个jpg图像
im = Image.open('1.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.GaussianBlur(10))
im2.save('blur.jpg', 'jpeg')