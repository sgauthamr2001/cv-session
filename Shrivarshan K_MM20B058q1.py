#Question 1
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('/content/einstein.jpg')
blur_gaus1=cv2.GaussianBlur(img,(9,9),0)
blur_gaus2=cv2.GaussianBlur(img,(5,5),50)
finalimg=blur_gaus2-blur_gaus1
plt.figure(),plt.axis("off"),plt.title("Final Image"),plt.imshow(finalimg)
plt.show()