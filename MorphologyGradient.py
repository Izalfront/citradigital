import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\ImageNoise.jpg',0)

binr = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.ones((3,3), np.uint8)

invert = cv2.bitwise_not(binr)

#menggunakan morph gradient
morph_gradient = cv2.morphologyEx(invert,cv2.MORPH_GRADIENT,kernel)

plt.imshow(morph_gradient, cmap='gray')
plt.show()
