import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_rgb_histogram(image):
    # Pisahkan kanal RGB
    r, g, b = cv2.split(image)

    # Hitung histogram untuk setiap kanal
    hist_r, bins_r = np.histogram(r.flatten(), bins=256, range=[0, 256])
    hist_g, bins_g = np.histogram(g.flatten(), bins=256, range=[0, 256])
    hist_b, bins_b = np.histogram(b.flatten(), bins=256, range=[0, 256])

    # Plot histogram
    plt.figure(figsize=(15, 4))

    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.plot(hist_r, color='red')
    plt.title('Histogram Red Channel')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')

    plt.subplot(1, 4, 3)
    plt.plot(hist_g, color='green')
    plt.title('Histogram Green Channel')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')

    plt.subplot(1, 4, 4)
    plt.plot(hist_b, color='blue')
    plt.title('Histogram Blue Channel')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')

    plt.tight_layout()
    plt.show()

# Baca citra
image = cv2.imread('dataset\\monalisa.jpg')

# Tampilkan histogram RGB
plot_rgb_histogram(image)
