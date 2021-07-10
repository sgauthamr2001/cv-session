#Question 2
import cv2
barrel = cv2.imread('barrel.jpg')
barrel_hsv = cv2.cvtColor(barrel, cv2.COLOR_BGR2HSV)
histogram = cv2.calcHist([barrel_hsv], [0, 1], None, [100, 200], [0, 100, 0, 200])
cv2.normalize(histogram, histogram, 0, 255, cv2.NORM_MINMAX)
video = cv2.VideoCapture('video.mp4')

count, frame = video.read()
while count:
 frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 res = cv2.calcBackProject([frame_hsv], [0, 1], histogram, [0, 180, 0, 256], 1)
 disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
 cv2.filter2D(res, -1, disc, res) 
 ret,thresh = cv2.threshold(res, 150,255, cv2.THRESH_BINARY)
 final = cv2.merge((thresh, thresh, thresh))
 result = cv2.bitwise_and(frame, final)
 cv2.imshow( 'final result',result)

