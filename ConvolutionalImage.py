import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dataset\\semangka.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img, -1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Citra Asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst),plt.title('Konvolusi/Pelembutan Citra')
plt.xticks([]), plt.yticks([])
plt.show()