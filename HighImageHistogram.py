import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    #hitung histogram citra
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    #plot histogram
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.plot(hist, color='black')
    plt.title('Histogram')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')
    plt.tight_layout()
    plt.show()

#Baca citra
image = cv2.imread('dataset\\highcontrast.jpg', cv2.IMREAD_GRAYSCALE)

#tampilkan histogram citra low contrast
plot_histogram(image)