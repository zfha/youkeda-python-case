from PIL import Image, ImageDraw
import util
import face_recognition  # 引入face_recognition的库

image = face_recognition.load_image_file("shuihu/鲁智深.jpeg")  # 用这个库加载1.jpg图片
face_landmarks_list = face_recognition.face_landmarks(image)  # 获取图片的面部特征位置

origin = Image.fromarray(image)

# 获取第一个小女孩的五官信息
for face_landmarks in face_landmarks_list:
    browPoint = util.getBrowPoint(face_landmarks)
    chin = face_landmarks['chin']
    leftPoint, rightPoint = util.getLeftRightPoint(chin)

    hat = Image.open('christmas_hat.png')
    width, height = hat.size

    newWidth = int(rightPoint[0]) - int(leftPoint[0])
    newHeight = int(newWidth / width * height)
    box = (int(leftPoint[0]), int(browPoint[1]) - newHeight, int(rightPoint[0]), int(browPoint[1]))
    resizeHat = hat.resize((newWidth, newHeight))

    origin.paste(resizeHat, box, resizeHat)

origin.save('result.jpg')

