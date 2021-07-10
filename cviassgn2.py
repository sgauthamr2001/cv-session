import cv2
import numpy as np
from matplotlib import pyplot as plt
normImg=np.array([])
img=cv2.imread('../barrel.jpeg')
hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
vid=cv2.VideoCapture('../igvcvideo.mp4')
while True:
    break
    # Capture frame-by-frame
    ret, frame = vid.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    hsvVideo=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Display the resulting frame
    cv2.imshow('frame', hsvVideo)
    if cv2.waitKey(25) == ord('q'):
        break
# When everything done, release the capture
#vid.release()
#cv2.destroyAllWindows()
h,s,v=cv2.split(hsvImage)
imgHisth = cv2.calcHist([hsvImage], [0], None, [180], [0, 180])
imgHists = cv2.calcHist([hsvImage], [1], None, [256], [0, 256])
imgHistv = cv2.calcHist([hsvImage], [2], None, [256], [0, 256])
cv2.normalize(imgHisth,imgHisth, alpha=0, beta=180, norm_type=cv2.NORM_MINMAX)
cv2.normalize(imgHists,imgHists, alpha=0, beta=256, norm_type=cv2.NORM_MINMAX)
cv2.normalize(imgHistv,imgHistv, alpha=0, beta=256, norm_type=cv2.NORM_MINMAX)
resh = cv2.calcBackProject([hsvImage], [0], imgHisth, [0, 180], scale=1)
ress = cv2.calcBackProject([hsvImage], [1], imgHists, [0, 256], scale=1)
resv = cv2.calcBackProject([hsvImage], [2], imgHistv, [0, 256], scale=1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(resh, -1, disc, resh) #res is the matrix obtained after back projection
cv2.filter2D(ress, -1, disc, ress)
cv2.filter2D(resv, -1, disc, resv)
thh = cv2.adaptiveThreshold(resh,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
ths = cv2.adaptiveThreshold(ress,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,1050)
thv = cv2.adaptiveThreshold(resv,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,500)

thresh = cv2.merge((thh,ths,thv))
result = cv2.bitwise_or(img, thresh)
plt.subplot(122),plt.imshow(result),plt.title("Result image"),plt.axis("off")
plt.show()