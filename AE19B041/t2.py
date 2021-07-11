import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.read('a.png')
imghsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v=cv2.VideoCapture(0)
while(True):
	ret, frame = v.read()
	f=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	h=cv2.calcHist([f],[0],None,[256],[0,256])
	norn=np.zeros((800,800))
	hnum=cv2.normalize(h,norn,0,256,cv2.NORM_MINMAX)
	res=cv2.calcBackProject([f],[0],hnum,[0,256],1)
	disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
	cv2.filter2D(res, -1, disc, res)
	result=cv2.bitwise_or(imghsv,res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break		





