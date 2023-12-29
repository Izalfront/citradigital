import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Masukkan gambar pasfoto anda
img = cv.imread('dataset\\akhrian.png',0)
img2 = img.copy()

#Masukkan gambar pasfoto anda dengan nama file berbeda
#dan hanya bagian wajah saja
template = cv.imread('dataset\\akhriancrop.JPG',0)
w, h = template.shape[::-1]

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    #Penerapan template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    #Jika menggunakan TM_SQDIFF atau TM_SQDIFF_NORMED, maka diambil nilai mininum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left,bottom_right,255,2)
    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.title('Matching Results'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()