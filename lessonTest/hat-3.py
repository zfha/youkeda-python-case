from PIL import Image, ImageDraw
import util
import face_recognition  # 引入face_recognition的库
image = face_recognition.load_image_file("1.jpg")  # 用这个库加载1.jpg图片
face_landmarks_list = face_recognition.face_landmarks(image)  # 获取图片的面部特征位置

# 获取第一个小女孩的五官信息
face_landmarks = face_landmarks_list[0]

# 获取小女孩的左眼信息
left_eye = face_landmarks['left_eye']
right_eye = face_landmarks['right_eye']

leftPoint, rightPoint = util.getLeftRightPoint(left_eye)
leftCenterPoint = util.getCenter(leftPoint, rightPoint)

leftPoint, rightPoint = util.getLeftRightPoint(right_eye)
rightCenterPoint = util.getCenter(leftPoint, rightPoint)

print('左眼中心的点: ' + str(leftCenterPoint) + '右眼中心的点：' + str(rightCenterPoint))

centerPoint = util.getCenter(leftCenterPoint, rightCenterPoint)
print('整个眼睛中心的点：' + str(centerPoint))

browPoint = (centerPoint[0], centerPoint[1] - (rightCenterPoint[0] - leftCenterPoint[0]) * 1.2)
print('额头的顶部点：' + str(browPoint))

# 开始划线
origin = Image.fromarray(image)
draw = ImageDraw.Draw(origin)
draw.line([(browPoint[0] - 5, browPoint[1]), (browPoint[0] + 5, browPoint[1])])
draw.line([(browPoint[0], browPoint[1] - 5), (browPoint[0], browPoAint[1] + 5)])

origin.save('result.jpg')