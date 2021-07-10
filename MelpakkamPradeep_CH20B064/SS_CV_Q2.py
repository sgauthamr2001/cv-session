# importing libraries
import cv2
import numpy as np

barrel = cv2.imread(r"b2.png", 1)
cv2.cvtColor(barrel, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([barrel], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

barrel = cv2.cvtColor(barrel, cv2.COLOR_BGR2HSV)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(r'barrelvid.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video  file")

# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        res = cv2.calcBackProject([frame], [0, 1], hist, [0, 180, 0, 256], 1)
        disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        cv2.filter2D(res, -1, disc, res)  # res is the matrix obtained after back projection

        #Traffic Cone Orange is selected as colour to identify the cones since some other cones also are white
        retr, threshr = cv2.threshold(res, thresh= 250, maxval= 255, type = cv2.THRESH_BINARY)
        retg, threshg = cv2.threshold(res, thresh=105, maxval=255, type=cv2.THRESH_BINARY)
        retb, threshb = cv2.threshold(res, thresh=0, maxval=40, type=cv2.THRESH_TOZERO_INV)
        final = cv2.merge((threshr, threshg, threshb))
        result = cv2.bitwise_or(frame, final)

        # Display result
        cv2.imshow('Final result (Press \'q\' to exit)', result)
        # Press Q on keyboard to  exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        # Read next frame
        rval, frame = cap.read()

# Free-up memory
cap.release()





