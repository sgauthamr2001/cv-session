import cv2

barrel = cv2.imread('barrel.jpg')
barrel_hsv = cv2.cvtColor(barrel, cv2.COLOR_BGR2HSV)

target_histogram = cv2.calcHist([barrel_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(target_histogram, target_histogram, 0, 255, cv2.NORM_MINMAX)
capture = cv2.VideoCapture('video.mp4')

True_condition = True

while True_condition:
	True_condition, frame = capture.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	back_proj = cv2.calcBackProject([hsv_frame], [0, 1], target_histogram, [0, 180, 0, 256], 1)
	convol = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
	cv2.filter2D(back_proj, -1, convol, back_proj)
	_,thresh = cv2.threshold(back_proj, 20,255, cv2.THRESH_BINARY)
	final = cv2.merge((thresh, thresh, thresh))
	result = cv2.bitwise_and(frame, final)
	cv2.imshow( 'final result',result)

	if cv2.waitKey(30) == 27: #esc character
		break
