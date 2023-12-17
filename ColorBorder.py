import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('dataset/this.png')

#membuat border pada citra
constant = cv2.copyMakeBorder(img1,155,155,155,155,cv2.BORDER_CONSTANT)

#atur plot/tata letak untuk citra asli
plt.subplot(231),plt.imshow(img1, 'gray'),plt.title('CITRA BORDER')

#atur plot/tata letak untuk citra hasil border
plt.subplot(232),plt.imshow(constant,'gray'),plt.title('CITRA BORDER')

plt.show()


