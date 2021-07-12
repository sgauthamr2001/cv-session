import cv2

img = cv2.imread('Barrel_img.png')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

net = cv2.calcHist([img_hsv], [0, 1], None, [
    100, 200], [0, 100, 0, 200])


cv2.normalize(net, net, 0, 255, cv2.NORM_MINMAX)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))


video = cv2.VideoCapture('test-video.mp4')

if video.isOpened():
    count, static_img = video.read()
    while count:
        output_frame = cv2.cvtColor(static_img, cv2.COLOR_BGR2HSV)
        res = cv2.calcBackProject([output_frame], [0, 1], net, [
                                  0, 100, 0, 255], scale=1)
        cv2.filter2D(res, -1, disc, res)
        ret, thresh = cv2.threshold(
            res, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
        final = cv2.merge((thresh, thresh, thresh))
        result = cv2.bitwise_or(static_img, final)

        cv2.imshow('Press \'e\' to Exit', result)

        if ord('e') == cv2.waitKey(1):
            break

        count, static_img = video.read()
