import cv2
import numpy as np

image= cv2.imread("G_ISLEME\Tresholding\joker.png",0) # gri tonlama gerekiyor..

image=cv2.blur(image,(3,3)) # daha belirgin
#simple thresholding
ret,tresh1= cv2.threshold(image,160,255,cv2.THRESH_BINARY)
#adaptivethresholding
tresh2= cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    cv2.THRESH_BINARY,11,2)

tresh3= cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,11,2)

cv2.imshow("orijinal",image)
cv2.imshow("simple thresholding",tresh1)
cv2.imshow("adaptivethresholding_mean",tresh2) # ortalamasını alıyor daha temiz bir görüntü
cv2.imshow("adaptivethresholding_gauss",tresh3) # mean e göre daha ince detay


cv2.waitKey(0)
cv2.destroyAllWindows()