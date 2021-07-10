import cv2

einstein = cv2.imread("einstein.jpg")

einstein_1 = cv2.GaussianBlur(einstein, (5,5), 0)
einstein_2 = cv2.GaussianBlur(einstein, (9,9), 9)
einstein_edge = cv2.subtract(einstein_1, einstein_2)

cv2.imshow("edge", einstein_edge)

cv2.waitKey()
