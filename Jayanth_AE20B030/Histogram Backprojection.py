import cv2


def back_projection(target):
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
    res = cv2.calcBackProject([target_hsv], [0, 1],
                              img_hist, [0, 256, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cv2.filter2D(res, -1, disc, res)
    retr, thresh1 = cv2.threshold(res, 50, 255, cv2.THRESH_BINARY)
    retr, thresh2 = cv2.threshold(res, 50, 255, cv2.THRESH_TOZERO)
    retr, thresh3 = cv2.threshold(res, 50, 255, cv2.THRESH_TOZERO_INV)
    final = cv2.merge((thresh1, thresh2, thresh3))
    result = cv2.bitwise_or(final, target)
    return result


img = cv2.imread('barrel1.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hist = cv2.calcHist([img_hsv], [0, 1], None, [256, 256], [0, 256, 0, 256])
cv2.normalize(img_hist, img_hist, 0, 255, cv2.NORM_MINMAX)
vid = cv2.VideoCapture('srcvideo.mp4')
while vid.isOpened():
    ret, tar = vid.read()
    if ret:
        resu = back_projection(tar)
        cv2.imshow("Back Projection", resu)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
