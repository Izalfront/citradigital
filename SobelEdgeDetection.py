import numpy as np
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images

image = camera()
edge_sobel = filters.sobel(image) #penyaringan dengan sobel

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(6,3)) #atur tampilan gambar
axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[1].set_title('Metode Deteksi Tepi Sobel')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()