import cv2
import numpy as np

resim1 = cv2.imread("AGIRLIKLITOPLAMA\sari.jpg")
resim2 = cv2.imread("AGIRLIKLITOPLAMA\yaprak.jpg")

print(resim1[100,200]) #piksellerin renkleri
print(resim2[50,30])

cv2.imshow("Muz",resim1)
cv2.imshow("yaprak",resim2)

print(resim1[100,200]+resim2[50,30])


cv2.waitKey(0)
cv2.destroyAllWindows()

