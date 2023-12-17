import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\DilasidanErosiCitra.jpg',0)

biner = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.ones((3,3), np.uint8)

invert = cv2.bitwise_not(biner)

dilation = cv2.dilate(invert, kernel, iterations=1)

plt.imshow(dilation, cmap='gray')
plt.show()