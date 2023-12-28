import cv2 
import numpy as np

image1 = cv2.imread('dataset\\InputanAdaptiveThresholding.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# menerapkan ambang batas yang berbeda dengan adaptive mean dan gaussian
thresh1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,199,5)
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,199,5)

cv2.imshow('Adaptive Mean',thresh1)
cv2.imshow('Adaptive Gaussian',thresh2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()