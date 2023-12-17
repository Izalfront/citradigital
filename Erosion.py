import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dataset\\DilasidanErosiCitra.jpg',0)

#binerkan citra
biner = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

#menentukan kernel
kernel = np.ones((5,5), np.uint8)

#membalikkan citra
invert = cv2.bitwise_not(biner)

#mengikis citra
erosion = cv2.erode(invert, kernel,iterations=1)

plt.imshow(erosion, cmap='gray')
plt.show()