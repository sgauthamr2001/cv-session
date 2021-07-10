# -*- coding: utf-8 -*-
"""Task-2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n47vgvj5YYFx5WsDA0F_ygWAeFvQ2_fY
"""

pip install pafy

pip install youtube-dl

import cv2, pafy
from matplotlib import pyplot as plt
import youtube_dl
from google.colab.patches import cv2_imshow

url = "https://www.youtube.com/watch?v=A9BVr7kltl8"
video = pafy.new(url)
play = video.getbest()
cap = cv2.VideoCapture(play.url)

roi=cv2.imread('/content/sample_data/img_barrels.jpg')
rimg=cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
ob=cv2.calcHist([rimg],[0,2],None,[180,256],[0,180,0,256])
cv2.normalize(ob,ob,0,255,cv2.NORM_MINMAX)
while True:
  ret,frame =cap.read()
  img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  res=cv2.calcBackProject([img],[0,2],ob,[0,180,0,256],1)
  disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
  cv2.filter2D(res, -1, disc, res)
  _,thresh = cv2.threshold(res,10,255,cv2.THRESH_BINARY)
  final=cv2.merge((thresh,thresh,thresh))
  result= cv2.bitwise_or(frame,final)
  cv2_imshow(result)
cap.release()
cv2.destroyAllWinfows()

