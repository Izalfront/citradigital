import cv2
import numpy as np

img1 = cv2.imread('dataset\\input1.png')
img2 = cv2.imread('dataset\\input2.png')

dest_xor = cv2.bitwise_xor(img1, img2, mask = None)

cv2.imshow('Operasi XOR pada Citra', dest_xor)

cv2.waitKey(0)