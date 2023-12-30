import cv2 
import numpy as np

# Masukkan dataset haarcascade_frontalface_default
faceDetect = cv2.CascadeClassifier('dataset\\haarcascade_frontalface_default.xml')

# Melakukan akuisisi citra
camera = cv2.VideoCapture(0)
while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Cetak blok persegi berwarna hijau muda dengan kode RGB 0,255,0
        # Cetak blok di area wajah saja
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Tampilkan hasil pelacakan
    cv2.imshow('Hasil Pelacakan Wajah', img)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
