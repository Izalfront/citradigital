import cv2

# Tentukan nomor port kamera atau nama file video
cam_port = 0  # Ganti dengan nomor port yang sesuai

# Buat objek VideoCapture
cam = cv2.VideoCapture(cam_port)

# Periksa apakah objek VideoCapture berhasil dibuat
if not cam.isOpened():
    print("Error: Could not open camera.")
else:
    # Baca frame dari kamera
    result, image = cam.read()

    if result:
        # Tampilkan citra
        cv2.imshow("Akuisisi Citra", image)

        # Simpan citra
        cv2.imwrite("Inihasilakusisicitra.png", image)

        # Tunggu sampai pengguna menekan tombol keyboard
        cv2.waitKey(0)

        # Tutup jendela citra
        cv2.destroyAllWindows()
    else:
        print("GAMBAR TIDAK TERDETEKSI. COBA LAGI")

# Selalu jangan lupa melepaskan kamera setelah selesai menggunakan
cam.release()
