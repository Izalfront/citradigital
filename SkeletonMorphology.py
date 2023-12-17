from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

#Akusisi data gambar kuda
image = invert(data.horse())

#pengaturan kinerja skeletonization
skeleton = skeletonize(image)

#memunculkan visualisasi
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4),sharex=True, sharey=True)

ax = axes.ravel()
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('Citra asli', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('citra skeleton', fontsize=20)

fig.tight_layout()
plt.show()