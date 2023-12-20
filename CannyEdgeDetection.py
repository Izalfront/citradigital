import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature

#Menghasilkan gambar persegi yang memiliki noise
image = np.zeros((128,128), dtype=float)
image[32:-32,32:-32] = 1

image = ndi.rotate(image, 15, mode='constant')
image = ndi.gaussian_filter(image,4)
image = random_noise(image, mode='speckle', mean=0.1)

#hitung filter canny untuk dua nilai sigma
edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=3)

#menampilkan visualisasi hasil canny
fig, ax = plt.subplots(nrows=1,ncols=3,figsize=(8,3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title(r'Citra Asli Noise', fontsize=10)

ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Hasil Filter Deteksi Canny, $\sigma=1$', fontsize=10)

ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Hasil Filter Deteksi Canny, $\sigma=3$', fontsize=10)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()