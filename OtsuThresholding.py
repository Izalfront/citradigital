import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('dataset\\naskahkuno.jpg',0)

ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

#proses Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#thresholding Otsu's setelah penyaringan dengan rumus gaussian
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#plot semua gambar dan histogramnya
images = [img, 0, th1,
          img,0,th2,
          blur,th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian Filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(2):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]),plt.yticks([])
plt.show()