import cv2 
import numpy as np

imagel = cv2.imread('dataset\\DaunGanja.jpg')

# cv2.cvtColor digunakan untuk melakukan konversi color space
# untuk mengonversi gambar dalam skala abu-abu
img = cv2.cvtColor(imagel,cv2.COLOR_BGR2GRAY)

#menerapkan ambang batas yang berbeda
#teknik pada gambar input
#semua nilai piksel di atas 120 akan disetel ke 255
ret, thresh1 = cv2.threshold(img, 120,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyWindow()