
import matplotlib.pyplot as plt
import cv2

img='/home/naveen/Random/Einstein.jpg'
img=cv2.imread(img)
blur_gaus1 = cv2.GaussianBlur(img,(5,5),0.1)
blur_gaus2=  cv2.GaussianBlur(img,(9,9),10)
result=blur_gaus1-blur_gaus2

plt.figure(),plt.axis("off"),plt.title("Original Image"),plt.imshow(img)
plt.figure(),plt.axis("off"),plt.title("Blurred Image"),plt.imshow(result)
plt.show()
