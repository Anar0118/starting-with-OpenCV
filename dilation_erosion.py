import cv2 as cv

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
img = cv.resize(img, (750,500))
cv.imshow("Original Image", img)

# Canny Edges are used as a source for cv.dilate() for demonstration purposes
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilation - cv.dilate() 
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("Dilated Image:1", dilated)
# Trying different iteration number
#dilated = cv.dilate(canny, (3,3), iterations=5)
#cv.imshow("Dilated Image:2", dilated)

# Erosion - cv.erode()
eroded = cv.erode(dilated, (3,3), iterations=3) # Trying to get back to original image
cv.imshow("Eroded Image", eroded)


cv.waitKey(0)
