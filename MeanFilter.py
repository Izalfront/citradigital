import cv2
import numpy as np
from matplotlib import pyplot as plt

ori_img = cv2.imread('dataset\\GaussianNoiseImage.jpg')

def box_kernel(size):
    k = np.ones((size, size), np.float32) / (size ** 2)
    return k


kernel_size = 5
filtered_img = cv2.filter2D(ori_img, -1, box_kernel(kernel_size))

plt.subplot(121), plt.imshow(ori_img), plt.title('Citra asli')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_img), plt.title('citra yang diperhalus')
plt.xticks([]), plt.yticks([])
plt.show()
