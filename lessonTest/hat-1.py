from PIL import Image # 引入Pillow库
import face_recognition  # 引入face_recognition的库
image = face_recognition.load_image_file("1.jpg")  # 用这个库加载1.jpg图片
face_locations = face_recognition.face_locations(image) #  开始进行人脸识别
top, right, bottom, left = face_locations[0]

origin = Image.open('1.jpg')
out = origin.crop((left, top, right, bottom))
out.save('hat-1-result.jpg')