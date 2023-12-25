import cv2 as cv
import numpy as np

image = cv.imread('dataset\\elang.jpg')

#matriks kosong
blank = np.zeros(image.shape, dtype='uint8')

#mengkonversi ke grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#deteksi tepi
canny = cv.Canny(gray_image,215,275)

#mengidentifikasi contour
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#menggambar kontur pada gambar kosong
cv.drawContours(blank, contours, -1, (0, 255, 0), 1)

#tampilkan garis kontur pada gambar
cv.imshow('hasil citra deteksi countour',blank)

cv.waitKey(0)