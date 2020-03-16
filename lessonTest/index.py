import face_recognition
from PIL import Image, ImageFilter
# image = face_recognition.load_image_file("1.jpg")
# face_locations = face_recognition.face_locations(image)
#
# index = 1;
# for face_location in face_locations:
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#
#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.save('result' + str(index) + '.jpg')
#     index += 1
from PIL import Image, ImageFilter
im = Image.open('1.jpg')
out = im.filter(ImageFilter.BLUR)
out.save('result-detail.jpg')