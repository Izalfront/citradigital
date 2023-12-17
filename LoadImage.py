import cv2

filepath = r'dataset\\1130896.jpg'

image = cv2.imread(filepath)

cv2.imshow("ini adalah citra diakusisi",image)
cv2.waitKey(0)

output = 'dataset\\this is cogilll kont.png'
cv2.imwrite(output, image)

print("[INFO] berhasil {}".format(output))