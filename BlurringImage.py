import cv2
import numpy as np

img =cv2.imread('dataset\\this.png',0)

Gaussian = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('GaussianBlur',Gaussian)
cv2.waitKey(0)

#Median Blur
Median = cv2.medianBlur(img,5)
cv2.imshow('MedianBlur',Median)
cv2.waitKey(0)

#Billateral Blur
Bilateral = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('BillateralBlur',Bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()