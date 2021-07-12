#!/usr/bin/python3

import cv2

img_path = "../../media/einstein.jpg" # get the path of the image

img = cv2.imread(img_path, 0) # open the image as a grayscale image

gblur5 = cv2.GaussianBlur(img, (5, 5), 0) # gaussian blur with kernel size 5x5
gblur9 = cv2.GaussianBlur(img, (9, 9), 0) # gaussian blur with kernel size 9x9

edges = cv2.subtract(gblur5, gblur9) # take the difference
bright_edges = cv2.equalizeHist(edges) # equalize for better brightness

cv2.imshow("Edge Detection", bright_edges) # show the image

cv2.waitKey(0) # wait for any key
cv2.destroyAllWindows() # destroy all open windows