import cv2
import numpy as np

image= cv2.imread("G_ISLEME\Tresholding\joker.png",0) # gri tonlama gerekiyor..

#simple thresholding
ret1,tresh1= cv2.threshold(image,160,255,cv2.THRESH_BINARY)
#otsu thresholding
ret2,tresh2= cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("orijinal",image)
cv2.imshow("simple thresholding",tresh1)
cv2.imshow("otsu thresholding",tresh2) # orijinal resme daha yakın


cv2.waitKey(0)
cv2.destroyAllWindows()