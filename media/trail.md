# Problem Statement - CV Session-1

## Task 1: Edge Detection using Difference of Gaussians

In the session we have come across the Gaussian Filter for blurring an image. If you use two Gaussians filters of different sizes (having different standard deviations) and find their difference, it acts like a band pass filter and can detect edges. 

So try this out on the following image:

![](https://github.com/sgauthamr2001/cv-session/blob/main/media/einstein.jpg)

Perform Gaussian Blurring with kernels of size 5x5 and 9x9 and find their difference and see the output. 

## Task 2: Template Matching using Histograms

The task is to recognise the orange and white barrels in this [video](https://www.youtube.com/watch?v=A9BVr7kltl8). You will be using histogram backprojection to do so. Try to understand how 'cv2.calcBackProject()' works for this. 

The following are the steps you will roughly have to follow: 

* Get an image of the region of interest(the barrel), convert this to HSV from RGB. This is what you will be using for template matching. 

* Open your video using cv2.VideoCapture(), and convert your frame to HSV

* Calculate the histogram of your object using the cv2.calcHist() function. Normalize your histogram, and apply histogram backprojection using cv2.normalize() and cv2.calcBackProject(). 

* Let the result after calculating backproject be 'res'. Now to visualize 'res' better, we shall convolve with a circular disc.

``` 
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(res, -1, disc, res) #res is the matrix obtained after back projection
```

* Threshold your image. Try out different values for best results.

* Merge the thresholded matrices to get a 3 channel image

```
final = cv2.merge((thresh,thresh,thresh))
```

* Perform a bitwise or of 'final' with the target image and display the output

```
result = cv2.bitwise_or(target_img, final)
```

If this gives good results you can also go ahead and try to identify the white lines bounding the path. 
