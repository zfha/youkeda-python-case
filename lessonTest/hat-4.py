from PIL import Image, ImageDraw
import util
import face_recognition  # 引入face_recognition的库

image = face_recognition.load_image_file("1.png")  # 用这个库加载1.jpg图片
face_landmarks_list = face_recognition.face_landmarks(image)  # 获取图片的面部特征位置

hat = Image.open('christmas_hat.png')
width, height = hat.size

# 获取第一个小女孩的五官信息
face_landmarks = face_landmarks_list[0]

browPoint = util.getBrowPoint(face_landmarks)

chin = face_landmarks['chin']
leftPoint, rightPoint = util.getLeftRightPoint(chin) # 计算的左右边界


left = int(leftPoint[0])
right = int(rightPoint[0])
newWidth = right - left
newHeight = int(newWidth / width * height) # 高度按原来宽高的比例放缩
bottom = int(browPoint[1]) # 下边界等于额头中心的Y轴点
top = bottom - newHeight # 上边界等于下边界减去高度

print('left:' + str(left) + ' right:' + str(right))
print('top:' + str(top) + ' bottom:' + str(bottom))
print('width:' + str(width) + ' height:' + str(height))

resizeHat = hat.resize((newWidth, newHeight))
origin = Image.fromarray(image)
origin.paste(resizeHat, (left, top, right, bottom), resizeHat)
origin.save('result.jpg')