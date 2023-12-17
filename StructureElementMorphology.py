import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from skimage.morphology import diamond #import diamond pada skimage morfologi

#melakukan generate struktur elemen untuk 2D diamond
struc_2d = {
    'diamond(1)': diamond(1),
    'diamond(2)': diamond(2),
    'diamond(3)': diamond(3),
    'diamond(4)': diamond(4),
    'diamond(5)': diamond(5),
    'diamond(6)': diamond(6),
    'diamond(7)': diamond(7),
    'diamond(8)': diamond(8),
    'diamond(9)': diamond(9),
    'diamond(10)': diamond(10)
}

#memvisualisasikan masing-masing elemen
fig = plt.figure(figsize=(15,10))

idx = 1
for title, struc in struc_2d.items():
    ax = fig.add_subplot(2,5,idx)
    ax.imshow(struc,cmap='summer', vmin=0, vmax=2, zorder=2)
    for i in range(struc.shape[0]):
        for j in range(struc.shape[1]):
            ax.text(j,i,struc[i,j], ha='center', va='center', color='w', zorder=3)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.grid()
    ax.set_axisbelow(True)
    ax.set(xlim=(-1, struc.shape[0]), ylim=(-1,struc.shape[0]))
    ax.set_title(title)
    idx += 1

fig.tight_layout()
plt.savefig('diamond.png', dpi=100) #simpan gambar dalam bentuk file .png
plt.show()