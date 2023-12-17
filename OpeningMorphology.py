import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('dataset\\ImageNoise.jpg',0)

biner = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(biner,cv2.MORPH_OPEN,kernel,iterations=1)

plt.imshow(opening, cmap='gray')
plt.show()