import cv2 as cv
import numpy as np

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
img = cv.resize(img, (750,500))
ddepth = -1
ind = 0

while True:
        
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)
        
        dst = cv.filter2D(img, ddepth, kernel)
        
        cv.imshow("Filtered", dst)
        c = cv.waitKey(500)
        if c == 27:
            break
        ind += 1

# Program can be stopped by KeyboardInterrupt from terminal