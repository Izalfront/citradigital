import cv2

img = cv2.imread('dataset\\this.png', cv2.IMREAD_UNCHANGED)

dimensions = img.shape

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('dimensions:', dimensions)
print('Image Height: ', height)
print('Image Width: ', width)
print('Channels: ', channels)