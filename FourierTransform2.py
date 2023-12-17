import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread('dataset\\sobel.jpg',0)
dft = cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Citra Masukan'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Hasil Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()