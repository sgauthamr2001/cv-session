import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('einstein.jpg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred5 = cv2.GaussianBlur(imggray, (5, 5), 0)
blurred9 = cv2.GaussianBlur(imggray, (9, 9), 0)
canny5 = cv2.Canny(blurred5,20,50)
canny9 = cv2.Canny(blurred9,20,50)

plt.figure(),plt.imshow(blurred5,cmap='gray'),plt.axis('off'),plt.title('Original')
plt.figure(),plt.imshow(canny5,cmap='gray'),plt.axis('off'),plt.title('Edges Detected by Canny (5x5)')
plt.figure(),plt.imshow(canny9,cmap='gray'),plt.axis('off'),plt.title('Edges Detected by Canny (9x9)')
plt.show()
