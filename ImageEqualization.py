import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    #Konversi citra ke skala abu-abu jika berwarna
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #hitung histogram citra
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])

    #hitung probabilitas distribusi piksel
    prob = hist / float(image.size)

    #hitung nilai kumulatif distribusi probabilitas
    cum_prob = prob.cumsum()

    #hitung transformasi histogram
    equalized_image = np.interp(image.flatten(), bins[:-1], cum_prob*255)
    equalized_image = equalized_image.reshape(image.shape).astype(np.uint8)

    #hitung histogram citra hasil equalisasi
    equalized_hist, _= np.histogram(equalized_image.flatten(), bins=256, range=[0,256])

    #plot histogram sebelum dan setelah equalisasi
    plt.figure(figsize=(5,4))
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('hasil equalisasi histogram')
    plt.axis('off')
    plt.tight_layout()

    #plot histogram
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(hist, color='black')
    plt.title('histogram sebelum equalisasi')
    plt.xlabel('intensitas piksel')
    plt.ylabel('Jumlah piksel')
    plt.subplot(1,2,2)
    plt.plot(equalized_hist, color='black')
    plt.title('Histogram Setelah Equalisasi')
    plt.xlabel('intensitas piksel')
    plt.ylabel('jumlah piksel')
    plt.tight_layout()

    plt.show()

#baca citra
image = cv2.imread('dataset\\monalisa.jpg', cv2.IMREAD_GRAYSCALE)

#proses histogram equalization
equalized_image = histogram_equalization(image)