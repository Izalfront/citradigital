import cv2
import numpy as rizal

filepath = 'dataset\\this.png'
image = cv2.imread(filepath)

image_norm = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('original image', image)

cv2.imshow('rotate image', image_norm)

cv2.waitKey(0)
cv2.destroyAllWindows()