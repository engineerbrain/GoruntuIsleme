# BGR Mantığı

import re
import cv2
import numpy as np

resim1 = cv2.imread("bmw.png") 
resim2 = cv2.imread("yanardag.jpg") 

cv2.imshow("Fatch",resim2)

#print(resim) #Resmin matrisini gösterir. 
print(resim1.size) # Resmin boyutu
print(resim1.dtype) #Veri tipi
print(resim1.shape)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
