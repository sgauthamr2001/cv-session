import cv2
from matplotlib import pyplot as plt

img = cv2.imread('einstein.jpg')
blur_gauss1 = cv2.GaussianBlur(img, (9, 9), 0)
blur_gauss2 = cv2.GaussianBlur(img, (5, 5), 0)
img1 = blur_gauss2 - blur_gauss1
plt.figure(), plt.axis("off"), plt.title("Edge Detection using Gaussian Filters"), plt.imshow(img1)
plt.show()
