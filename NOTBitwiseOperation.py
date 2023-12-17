import cv2
import numpy as np

img1 = cv2.imread('dataset\\input1.png')
img2 = cv2.imread('dataset\\input2.png')

dest_not1 =cv2.bitwise_not(img1, mask= None)
dest_not2 = cv2.bitwise_not(img2, mask= None)

cv2.imshow('ini adalah not citra 1',dest_not1)
cv2.imshow('ini adalah not citra 2',dest_not2)

cv2.waitKey(0)