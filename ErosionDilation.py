import cv2
import numpy as np

img = cv2.imread('dataset\\DilasidanErosiCitra.jpg', 0)  # Membaca citra dalam mode grayscale

# Mengambil matriks ukuran 5x5 sebagai kernel
kernel = np.ones((5, 5), np.uint8)

# Proses erosi dengan 1 kali iterasi pengikisan
img_erosion = cv2.erode(img, kernel, iterations=1)

# Proses dilasi dengan 1 kali iterasi pengikisan
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Citra Asli', img)
cv2.imshow('Hasil Erosion', img_erosion)
cv2.imshow('Hasil Dilation', img_dilation)

cv2.waitKey(0)
