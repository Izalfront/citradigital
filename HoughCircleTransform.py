import cv2 as cv 
import numpy as np

img = cv.imread('dataset\\circleimage.png',0)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #gambar lingkaran luar
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    #gambar pusat lingkaran
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv.imshow('hasil deteksi pola lingkaran pada citra',cimg)
cv.waitKey(0)
cv.destroyAllWindows()