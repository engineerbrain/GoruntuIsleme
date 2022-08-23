import cv2
import numpy as np

image= cv2.imread("G_ISLEME\Tresholding\joker.png",0)

ret,tresh1= cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,tresh2= cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,tresh3= cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,tresh4= cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,tresh5= cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)





cv2.imshow("orijinal",image)
cv2.imshow("tresh1",tresh1)
cv2.imshow("tresh2",tresh2)
cv2.imshow("tresh3",tresh3)
cv2.imshow("tresh4",tresh4)
cv2.imshow("tresh5",tresh5)










cv2.waitKey(0)
cv2.destroyAllWindows()