# from PIL import Image, ImageDraw
# import face_recognition  # 引入face_recognition的库
# image = face_recognition.load_image_file("1.jpg")  # 用这个库加载1.jpg图片
# face_landmarks_list = face_recognition.face_landmarks(image)
#
# pil_image = Image.fromarray(image)
# d = ImageDraw.Draw(pil_image)
#
# face_landmarks = face_landmarks_list[0]
#
# # Print the location of each facial feature in this image
# for facial_feature in face_landmarks.keys():
#     print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
#
# # Let's trace out each facial feature in the image with a line!
# # for facial_feature in face_landmarks.keys():
#     d.line(face_landmarks['chin'], width=5)
#
# pil_image.save('hat-2-result.jpg')
#


from PIL import Image, ImageDraw
import face_recognition  # 引入face_recognition的库
image = face_recognition.load_image_file("rulai.jpg")  # 用这个库加载1.jpg图片
face_landmarks_list = face_recognition.face_landmarks(image)  # 获取图片的面部特征位置

# 开始划线
origin = Image.fromarray(image)
draw = ImageDraw.Draw(origin)
# 获取第一个小女孩的五官信息
face_landmarks = face_landmarks_list[0]
# 获取小女孩的脸轮廓信息
for mark in face_landmarks:
    draw.line(face_landmarks[mark])

print('------')
print(face_landmarks_list)
origin.save('result.jpg')
#
