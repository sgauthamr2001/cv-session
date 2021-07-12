import cv2
import matplotlib.pyplot as plt
img=cv2.imread("D:/iitm/Summer_school/Deep_Learning_Masterclass/einstein.jpg",0)
img1=cv2.GaussianBlur(img,(5,5),0)
img2=cv2.GaussianBlur(img,(9,9),0)
img_edge=img1-img2
plt.figure()
plt.imshow(img_edge,cmap="gray"),plt.title("EDGES"),plt.axis("off")
plt.show()