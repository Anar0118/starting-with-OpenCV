import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# Painting Image
""" 
blank[100:200, 100:200] = 0,0,255
cv.imshow("Red", blank)
"""
# Drawing Rectangle

cv.rectangle(blank, (blank.shape[1]//2 - 100, blank.shape[0]//2 - 100), (blank.shape[1]//2 + 100, blank.shape[0]//2 + 100), (0,255,0), thickness=cv.FILLED)
#cv.imshow("Rectangle", blank)

# Drawing Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness=cv.FILLED)
#cv.imshow("Circle", blank)

# Drawing Line
cv.line(blank, (blank.shape[1]//2 - 100, blank.shape[0]//2 - 100), (blank.shape[1]//2 + 100, blank.shape[0]//2 + 100), (255,0,0), thickness=2)
#cv.imshow("All in One", blank)

# Writing Text
cv.putText(blank, "All in One", (165, 450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow("All in One", blank)

cv.waitKey(0)