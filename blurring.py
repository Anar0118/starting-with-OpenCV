import cv2 as cv

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
img = cv.resize(img, (750,500))
cv.imshow("Original Image", img)

# Averaging - cv.blur()
average = cv.blur(img, (7,7))
cv.imshow("Average Blur:1", average)
# Changing Kernel size
average = cv.blur(img, (7,7))
#cv.imshow("Average Blur:2", average)

# Gaussian Blur - cv.GaussianBlur()
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur - cv.medianBlur()
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

# Bilateral Blur - cv.bilateralFilter()
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)