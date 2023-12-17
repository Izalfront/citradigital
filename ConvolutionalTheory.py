import cv2 as cv
import scipy.signal as sig
import numpy as np
b=np.asarray([[4,7,1,9],
        [3,55,5,1],
        [2,2,8,2],
        [3,3,4,6]
        ],dtype=np.uint8)

w=np.asarray([[0,-1],
             [-1,4]],dtype=np.uint8)

w_r=np.asarray([[0,-1],
                [-1,4]],dtype=np.uint8)

print(sig.convolve2d(b,w,mode="same"))
kernel_r=np.asarray([[1,1,1],[1,1,2],[2,1,1]])
print('--------')
print(cv.filter2D(b,-1,w_r))