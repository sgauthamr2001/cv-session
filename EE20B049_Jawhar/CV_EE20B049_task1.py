import cv2
from matplotlib import pyplot as plt

# reading the image
img = cv2.imread(r'C:\Users\Jawhar\Downloads\einstein.jpg', 0)
# displaying the original image
plt.figure()
plt.imshow(img, cmap = 'gray'),plt.title("Original Image"),plt.axis("off")
# performing gaussian filtering with kernels of size 5 and 9 with different SDs.
blur_gauss1 = cv2.GaussianBlur(img,(5,5),0)
blur_gauss2 = cv2.GaussianBlur(img,(9,9),0.01)
# subtracting the two filtered images
sub = cv2.subtract(blur_gauss1,blur_gauss2)
# passing the subtracted image to canny function
canny = cv2.Canny(sub,100,75)
# displaying the edge detected image
plt.figure()
plt.imshow(canny, cmap = 'gray'),plt.title("Edge detected image:"),plt.axis("off")
plt.show()
