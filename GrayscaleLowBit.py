import cv2
import numpy as np

imageSource = 'dataset\\Figure_1.png'
original_img = cv2.imread(imageSource,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image ini',original_img)
result = original_img & 0b10000000
cv2.imshow('out',result)
cv2.imwrite('out.jpg',result)
cv2.waitKey(0)
cv2.destroyAllWindows()