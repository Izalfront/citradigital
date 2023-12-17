import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\this.png',0)

plt.imshow(img, cmap= 'binary', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()