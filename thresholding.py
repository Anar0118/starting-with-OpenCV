import cv2 as cv

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
img = cv.resize(img, (750,500))
cv.imshow("Original Picture", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Picture", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded Picture", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverse Thresholded Picture", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3) # can try cv.ADAPTIVE_THRESH_MEAN_C as adaptiveMethod 
cv.imshow("Adaptive Threshold", adaptive_thresh)

# Thresholding with inRange
hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_image, (0,0, 0), (250,250, 250))
result = cv.bitwise_and(img, img, mask=mask)

#cv.imshow("Mask", mask)
#cv.imshow("Result", result)

cv.waitKey(0)