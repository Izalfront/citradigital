import cv2

def detect_fire_live():

    # Masukkan dataset api dari file .xml
    fire_cascade = cv2.CascadeClassifier('dataset\\fire_tracking.xml')

    # Akusisi citra dengan open camera
    live_Camera = cv2.VideoCapture(0)

    while True:  # Perbaikan: Gunakan "True" dengan huruf besar
        # Baca setiap frame dari pengambilan video
        ret, frame = live_Camera.read()

        if not ret:
            break

        # Konversi frame menjadi skala keabuan
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Proses pelacakan api
        fires = fire_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Blok area api yang terlacak dengan bentuk persegi berwarna merah
        for (x, y, w, h) in fires:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Tampilkan hasil pelacakan
        cv2.imshow('Hasil Deteksi Titik Api', frame)  # Perbaikan: Gunakan nama yang jelas

        # Akhiri perulangan program dengan menekan tombol q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Lepaskan tangkapan video dan tutup semua jendela
    live_Camera.release()
    cv2.destroyAllWindows()

# Panggil fungsi untuk melacak api dari video secara real-time
detect_fire_live()
