# Assignment 2
## Task - 1
### Code - 
```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Images/einstein.jpg',0)
img2 = cv2.GaussianBlur(img, (5, 5), 0)
img3 = cv2.GaussianBlur(img, (9, 9), 1.8)
img5 = img3 - img2
plt.subplot(121),plt.imshow(img , cmap='gray'),plt.title("Orginal"),plt.axis("off")
plt.subplot(122),plt.imshow(img5 , cmap='gray'),plt.title("New"),plt.axis("off")
plt.show()
```
### Result :-
![](https://github.com/KushAg20/abcd/blob/main/Images/Einstein_New.png)  
--- ---
## Task - 2
### Code -
```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
vid = cv2.VideoCapture('video.mp4')
vid.set(cv2.CAP_PROP_POS_MSEC, 240000)
ret,frame = vid.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

bar = cv2.imread('Images/barral.png')
bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([bar], [0], None, [180], [0, 180])
norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)
plt.plot(norm)

res = cv2.calcBackProject([frame], [0], norm, [0, 180], 1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(res, -1, disc, res)

x, thresh = cv2.threshold(res, 36, 255, cv2.THRESH_BINARY)

final = cv2.merge((thresh, thresh, thresh))

plt.axis('off')
plt.imshow(cv2.bitwise_and(cv2.cvtColor(frame, cv2.COLOR_HSV2RGB), final))
plt.show()

```
#### Original Frame
![](https://github.com/KushAg20/abcd/blob/main/Images/frame.png)  

#### Result
![](https://github.com/KushAg20/abcd/blob/main/Images/Result.png)  

