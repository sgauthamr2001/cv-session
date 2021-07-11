import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("barrel.png")
imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
vid=cv2.VideoCapture(0)
while(True):
	reg,frame=vid.read()
	framehsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	hist=cv2.calcHist([framehsv],[0],None,[256],[0,256])
	norm=np.zeros((800,800))
	histnorm=cv2.normalize(hist,norm,0,256,cv2.NORM_MINMAX)
	res=cv2.calcBackProject([framehsv],[0],histnorm,[0,256],1)
	disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
	cv2.filter2D(res, -1, disc, res)
	result = cv2.bitwise_or(imghsv, res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
