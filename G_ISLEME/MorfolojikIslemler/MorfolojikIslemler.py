import cv2
import numpy as np

# resimlerdeki eksik kısmı tamamlar..

image=cv2.imread("G_ISLEME\MorfolojikIslemler\deniz1.png")

kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(image,kernel,iterations=1)
erosion = cv2.erode(image,kernel,iterations=1)

cv2.imshow("orijinal",image)
cv2.imshow("erosion",erosion) #aşındırma işlemi : Kalınlık ve boyut azalır..
cv2.imshow("dilation",dilation) # genişletme işlemi : Kalınlık ve boyut artar..

cv2.waitKey(0)
cv2.destroyAllWindows()