import cv2 
import os

# Masukkan dataset haarcascade_frontalface_default 
cascPath = "dataset/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Menangkap frame-by-frame
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Cetak blok persegi berwarna biru dengan kode RGB 0,0,255
    # Cetak blok di area wajah saja 
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Tampilkan frame pelacakan yang dihasilkan
    cv2.imshow('Hasil Pelacakan Wajah', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
