import cv2 as cv

img = cv.imread("OpenCV\Photos\Wallpaper.jpg")
img = cv.resize(img, (750,500))

t1 = cv.getTickCount() # Starting just before program execution

for i in range(5,49,2):
    img = cv.medianBlur(img,i)
t2 = cv.getTickCount() # Starting just after program termination

freq = cv.getTickFrequency()
t = (t2 - t1)/freq

print("Starting Cycle: {}\nEnding Cycle: {}\nFrequency: {} Hz\nRuntime: {} sec".format(t1, t2, freq, t))