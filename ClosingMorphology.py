import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\ImageNoise.jpg',0)

binr = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.ones((3,3), np.uint8)

closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE,kernel,iterations=1)

plt.imshow(closing, cmap='gray')
plt.show()