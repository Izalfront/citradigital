import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dataset\\ImageSegmentation.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,8))
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Citra Asli')
plt.show()

#mengkonversi ke citra grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,8))
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.title('Citra Grayscale')
plt.show()

#mengkonversi ke Binary Inverted Image
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
plt.figure(figsize=(8,8))
plt.imshow(thresh, cmap='gray')
plt.axis('off')
plt.title('Citra Threshold')
plt.show()

#proses segmentasu citra
kernel = np.ones((3,3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel,iterations=15)
bg = cv2.dilate(closing,kernel,iterations=1)
dist_transform = cv2.distanceTransform(closing,cv2.DIST_L2,0)
ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(),255,0)
cv2.imshow('image',fg)
plt.figure(figsize=(8,8))
plt.imshow(fg,cmap='gray')
plt.axis('off')
plt.title('Segmentasi Citra')
plt.show()

#hasil akhir segmentasi (rekapan proses)
plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Citra Asli')
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Citra Asli')
plt.imshow(img,cmap='gray')

plt.subplot(2,2,3)
plt.show(thresh,cmap='gray')
plt.axis('off')
plt.title('Citra Threshold')

plt.subplot(2,2,4)
plt.imshow(fg,cmap='gray')
plt.axis('off')
plt.title('Segmentasi Citra')

plt.show()