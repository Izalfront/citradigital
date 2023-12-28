import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_ubyte  # Import yang diperlukan
from skimage.filters import threshold_multiotsu

#Mengatur ukuran font untuk semua plot
matplotlib.rcParams['font.size'] = 9

#Memasukkan citra secara otomatis
image = data.camera()

#Menerapkan ambang batas nilai untuk multi-Otsu dengan nilai default
#Sehingga menghasilkan tiga kelas
threshold = threshold_multiotsu(image)

#Menggunakan nilai ambang batas, kami menghasilkan tiga wilayah
regions = np.digitize(image, bins=threshold)

fig, ax = plt.subplots(nrows=1,ncols=3,figsize=(10, 3.5))

#Merencakan gambar asli
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
ax[0].axis('off')

#Memplot histogram dan dua ambang yang diperoleh dari multi-otsu
ax[1].hist(image.ravel(), bins=255)
ax[1].set_title('Histogram')
for thresh in threshold:
    ax[1].axvline(thresh, color='r')

#Merencanakan hasil Multi Otsu
ax[2].imshow(regions, cmap='jet')
ax[2].set_title('Multi-Otsu result')
ax[2].axis('off')

plt.subplots_adjust()

plt.show()