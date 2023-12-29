import cv2 as cv 
image = cv.imread('dataset\\Shape.png')

#mengubah gambar menjadi mode skala keabuan
gray_image =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#temukan image thresholding
_, thrash = cv.threshold(gray_image, 240,255, cv.THRESH_BINARY)
contours,_ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour,True), True)
    x_cor = shape.ravel()[0]
    y_cor = shape.ravel()[1]

    #deteksi pola gambar segitiga
    if len(shape) == 3:
        cv.drawContours(image, [shape], 0, (0,0,0),4)
        cv.putText(image,"ini adalah segitiga", (x_cor,y_cor),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    if len(shape) ==5:
        cv.drawContours(image, [shape],0,(0,0,0),4)
        cv.putText(image,'ini adalah pentagon', (x_cor,y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    #deteksi pola gambar lingkaran
    if len(shape) > 12:
        cv.drawContours(image, [shape], 0,(0,0,0),4)
        cv.putText(image, 'ini adalah lingkaran', (x_cor, y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))

    #deteksi pola gambar trapesium
    if len(shape) == 4:
        x,y,w,h = cv.boundingRect(shape)
        aspect_ratio = float(w)/h
        if aspect_ratio >=1.2 and aspect_ratio <=2.0:
            cv.drawContours(image, [shape], 0,(0,0,0),4)
            cv.putText(image,'ini adalah trapesium', (x_cor,y_cor), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

cv.imshow('Hasil Deteksi Bentuk', image)
cv.waitKey(0)
cv.destroyAllWindows()