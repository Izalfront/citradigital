import cv2
import numpy as np

def denoise_median(image, window_size):
    return cv2.medianBlur(image, window_size)

def denoise_gaussian(image, kernel_size, sigma):
    return cv2.GaussianBlur(image,(kernel_size,kernel_size),sigma)

#ubah "nama_citra.jpg"sesuai dengan nama file citra yang ingin anda proses
nama_file_citra = 'dataset\\CitraLena.jpg'

#baca citra menggunakan OpenCv
citra_asli = cv2.imread(nama_file_citra, cv2.IMREAD_COLOR)

#konversi citra menjadi grayscale
citra_gray = cv2.cvtColor(citra_asli, cv2.COLOR_BGR2GRAY)

#atur ukuran jendela median filter (gunakan bilangan ganjil)
window_size_median = 5

#lakukan denoising menggunakan median filter
citra_hasil_median = denoise_median(citra_gray, window_size_median)

#atur ukuran kernel dan nilai sigma untuk gaussian filter
kernel_size_gaussian = 5
sigma = 1.5

#lakukan denoising menggunkan gaussian filter
citra_hasil_gaussian = denoise_gaussian(citra_gray, kernel_size_gaussian,sigma)

#tampilkan citra citra hasil denoising
cv2.imshow('citra asli', citra_gray)
cv2.imshow('denoising (median)',citra_hasil_median)
cv2.imshow('denoising (gaussian)',citra_hasil_gaussian)

#tunggu hingga tombol keyboard ditekan dan tutup jendela jika ditekan
cv2.waitKey(0)
cv2.destroyAllWindows()