import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
kernel = np.ones((3,3),np.uint8)
img = cv.imread("einstein.jpg",0)

blur1 = cv.GaussianBlur(img,(5,5),50)
blur2 = cv.GaussianBlur(img,(9,9),0)

diff= (blur1-blur2)


cv.imshow("diff",diff)
    #Press any key to exit
cv.waitKey(0)
