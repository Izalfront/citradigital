import cv2

image = cv2.imread('dataset\\this.png')

cv2.circle(image,(100,23),25,(0,255,0))
cv2.circle(image,(40,100),25,(0,0,255))
cv2.circle(image,(100,76),52,(255,0,0),3)
cv2.circle(image,(23,100),25,(0,255,0))
cv2.circle(image,(100,40),25,(0,0,255))
cv2.circle(image,(76,100),52,(255,0,0),3)

cv2.imshow('lingkaran gambar', image)
cv2.waitKey(0)
cv2.destroyAllWindows()