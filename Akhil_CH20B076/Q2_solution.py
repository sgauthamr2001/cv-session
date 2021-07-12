"""
CV-Session-1 Assignment
Question-2 Solution

By: P Akhil Reddy
Roll No: CH20B076
Contact: 8074147570
Email: ch20b076@smail.iitm.ac.in

Problem Statement: Template Matching using Histograms
"""
import cv2

#reads the input image
img = cv2.imread('barrel.png')

#converting the image to HSV color space using cvtColor function
cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#plots the histogram of img and then normalisation is done
img_hist = cv2.calcHist([img], [0, 1], None, [180, 255], [0, 180, 0, 255])
cv2.normalize(img_hist, img_hist, 0, 255, cv2.NORM_MINMAX)

#create a videocapture object and open the .mp4 file
vid = cv2.VideoCapture('video.mp4')

#print the error message if the video is not opened
if  (vid.isOpened()==False):
    print ("file can't be opened due to some error")


while (vid.isOpened()):

    #read frame by frame of the video
    ret, frame = vid.read()

    if ret:

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #converts the frame to hsv

        res = cv2.calcBackProject([frame_hsv], [0, 1], img_hist, [0, 180, 0, 256], 1)
        #calculates the backproject of the img_hist 

        disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        cv2.filter2D(res, -1, disc, res) #res is the matrix obtained after back projection

        #now we do the three thresholds
        retr, thresh1 = cv2.threshold(res, 240, 255, cv2.THRESH_BINARY)
        retg, thresh2 = cv2.threshold(res, 40, 255, cv2.THRESH_BINARY)
        retb, thresh3 = cv2.threshold(res, 0, 40, cv2.THRESH_TOZERO_INV)

        #merge the three thresholds and perform a bitwise or of 'final' with the target image
        final = cv2.merge((thresh1, thresh2, thresh3))
        result = cv2.bitwise_or(final, frame_hsv)

        #show result
        cv2.imshow("Back Projection, press q to exit", result)

        #press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()