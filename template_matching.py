import cv2 as cv

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
#cv.imshow("Wallpaper Before", img)

input_image = cv.resize(img, (750,500))
cv.imshow("Wallpaper After", input_image)

template = input_image[80:275, 250:350]
cv.imshow("Template", template)

gray_input = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)
gray_template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

result = cv.matchTemplate(gray_input, gray_template, cv.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv.minMaxLoc(result)
h, w = gray_template.shape
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(input_image, top_left, bottom_right, (0, 255, 0), 2)
cv.imshow('Matching Result', input_image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.waitKey(0)