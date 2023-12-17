import cv2

img = cv2.imread('dataset/this.png')

newImg = cv2.resize(img, (500, 300))

cv2.imshow('gambar baru', newImg)

cv2.waitKey(0)