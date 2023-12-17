import cv2
import numpy as np

img1 = cv2.imread('dataset\\input1.png')
img2 = cv2.imread('dataset\\input2.png')

dest_and = cv2.bitwise_and(img2, img1, mask= None)

cv2.imshow('Operasi AND pada Citra', dest_and)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()