import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    #pisahkan kanal RGB
    r, g, b = cv2.split(image)

    #Hitung histogram untuk setiap kanal
    hist_r, bins_r = np.histogram(r.flatten(), bins=256, range=[0,256])
    hist_g, bins_g = np.histogram(g.flatten(), bins=256, range=[0,256])
    hist_b, bins_b = np.histogram(b.flatten(), bins=256, range=[0,256])
    #plot histogram
    plt.figure(figsize=(5,5))

    plt.subplot(311)
    plt.hist(r.flatten(), bins=256, range=[0,256], color='r')
    plt.title('Red Channel')

    plt.subplot(312)
    plt.hist(g.flatten(), bins=256, range=[0,256], color='g')
    plt.title('Green Channel')

    plt.subplot(313)
    plt.hist(b.flatten(), bins=256, range=[0,256],color='b')
    plt.title('Blue Channel')

    plt.tight_layout()
    plt.show()

#membaca citra di dalam dataset
image = cv2.imread('dataset\\monalisa.jpg',0)

#konversi citra dari BGR ke RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#tampilkan histogram
plot_histogram(image_rgb)
                                  