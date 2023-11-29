import cv2 as cv
import numpy as np

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
#cv.imshow("Wallpaper Before", img)

resized = cv.resize(img, (750,500))
cv.imshow("Wallpaper After", resized)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(resized, -100, 100)
cv.imshow("Translated", translated)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(resized, -90)
cv.imshow("Rotated", rotated)


cv.waitKey(0)