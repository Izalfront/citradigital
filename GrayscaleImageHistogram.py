import cv2

from matplotlib import pyplot as plt

#mendapatkan img yang dipilih
img = cv2.imread('dataset\\CitraGrayscale.jpg',0)

#temukan frekuensi piksel dalam rentang 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

#menunjukan grafik plotting dari suatu gambar
plt.plot(histr)
plt.show()