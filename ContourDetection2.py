import cv2 as cv
import numpy as np

image = cv.imread('dataset\\ImageObject.jpg')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray,(3,3),0)
edged = cv.Canny(blurred,10,100)

#mendefinisikan (3,3) struktur elemen
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))

#menerapkan operasi dilation ke gambar tepi/edge detection
dilate = cv.dilate(edged,kernel,iterations=1)

#temukan kontur pada gambar yang didilasii/dilation
contours,_ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
image_copy = image.copy()
#cetak kontur pada salinan gambar aslinya
cv.drawContours(image_copy,contours, -1,(0,255,0),2)
print(len(contours), "Objek yang ditemukan dalam citra masukan ini.")

cv.imshow('Citra yang Dilasi', dilate)
cv.imshow('Hasil dari contour detection', image_copy)
cv.waitKey(0)