import cv2
import numpy

img = cv2.imread(r"C:\Users\MelPr\PycharmProjects\pythonProject1\einstein.jpg", 0)
blur_gaus_3 = cv2.GaussianBlur(img,(3,3),0)
blur_gaus_5 = cv2.GaussianBlur(img,(5,5),0)

img1 = blur_gaus_5 - blur_gaus_3
cv2.imshow(' ', img1)
cv2.waitKey(0)
