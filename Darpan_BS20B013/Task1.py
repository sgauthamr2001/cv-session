import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('einstien.png')  # image reading
img1 = cv2.GaussianBlur(img, (5, 5), 16)
img2 = cv2.GaussianBlur(img, (9, 9), 27)
net = img2-img1

obj, fin_img = cv2.threshold(net, 100, 255, cv2.THRESH_BINARY)


# printing out the image and its blurred difference
plt.subplot(221), plt.imshow(img, cmap='twilight'), plt.title(
    "Original Image"), plt.axis("off")
plt.subplot(222), plt.imshow(fin_img, cmap='twilight'), plt.title(
    "detected edge"), plt.axis("off")
plt.show()
