import cv2

img = cv2.imread('dataset\\this.png')

cv2.putText(img,'politeknik negeri banjarmasin', (30,30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255,255,255),2)

cv2.imshow('menuliskan teks pada citra',img)

cv2.waitKey(0)
cv2.destroyAllWindows()