import cv2

img = cv2.imread("./einstein.jpg")
img5 = cv2.GaussianBlur(img, (5, 5), 0, 0)
img9 = cv2.GaussianBlur(img, (9, 9), 0, 0)

final = img9 - img5

cv2.imshow("", final)
cv2.waitKey(0)
