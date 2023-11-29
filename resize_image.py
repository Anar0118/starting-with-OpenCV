import cv2 as cv

def rescale(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Resizing Images

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")

cv.imshow("Before", img)
resized_image = rescale(img,0.25)
cv.imshow("After", resized_image)

cv.waitKey(0)