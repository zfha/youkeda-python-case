from PIL import Image # 引入Pillow库
import face_recognition  # 引入face_recognition的库
image = face_recognition.load_image_file("1.jpg")  # 用这个库加载1.jpg图片
face_locations = face_recognition.face_locations(image) #  开始进行人脸识别

index = 1
for face_location in face_locations:
    origin = Image.open('1.jpg')
    top, right, bottom, left = face_location
    out = origin.crop((left, top, right, bottom))
    out.save('result' + str(index) + '.jpg')
    index += 1

