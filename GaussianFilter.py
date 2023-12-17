import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\GaussianNoiseImage.jpg')
ori_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def gaussian_kernel(size, sigma = 1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    normal = 1 / (2.0*np.pi*sigma**2)
    g = np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

sigma = 1
size = 5
filtered_img_1 = cv2.filter2D(ori_img, -1, gaussian_kernel(size, sigma))

filtered_img_2 = cv2.GaussianBlur(ori_img,(size,size),0)

plt.subplot(131), plt.imshow(ori_img), plt.title('Citra Asli')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(filtered_img_1), plt.title('Penghalusan citra tahap 1')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(filtered_img_2), plt.title('Penghalusan citra tahap 2')
plt.xticks([]), plt.yticks([])
plt.show()
