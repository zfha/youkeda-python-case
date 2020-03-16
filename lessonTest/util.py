def getLeftRightPoint(points):
    leftPoint = points[0]
    rightPoint = points[0]
    for point in points:
        if point[0] < leftPoint[0]:
            leftPoint = point
        if point[0] > rightPoint[0]:
            rightPoint = point

    return leftPoint, rightPoint


def getCenter(leftPoint, rightPoint):
    return (leftPoint[0] + rightPoint[0]) / 2, (leftPoint[1] + rightPoint[1]) / 2


# 获取小女孩的左眼信息
def getBrowPoint(face_landmarks):
    left_eye = face_landmarks['left_eye']
    right_eye = face_landmarks['right_eye']

    leftPoint, rightPoint = getLeftRightPoint(left_eye)
    leftCenterPoint = getCenter(leftPoint, rightPoint)

    leftPoint, rightPoint = getLeftRightPoint(right_eye)
    rightCenterPoint = getCenter(leftPoint, rightPoint)
    centerPoint = getCenter(leftCenterPoint, rightCenterPoint)
    browPoint = (centerPoint[0], centerPoint[1] - (rightCenterPoint[0] - leftCenterPoint[0]) * 1.2)
    return browPoint


def premultiply(im):
    pixels = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b, a = pixels[x, y]
            if a != 255:
                r = r * a // 255
                g = g * a // 255
                b = b * a // 255
                pixels[x, y] = (r, g, b, a)


def unmultiply(im):
    pixels = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b, a = pixels[x, y]
            if a != 255 and a != 0:
                r = 255 if r >= a else 255 * r // a
                g = 255 if g >= a else 255 * g // a
                b = 255 if b >= a else 255 * b // a
                pixels[x, y] = (r, g, b, a)
