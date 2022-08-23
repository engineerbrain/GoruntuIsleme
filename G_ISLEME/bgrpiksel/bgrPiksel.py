import cv2
import numpy as np

pacmanResmi = cv2.imread("pacman.jpg")

cv2.imshow("Pacman",pacmanResmi)

print(pacmanResmi[230,150])

print("Resmin Boyutu: " + str(pacmanResmi.size))
print("Resmin Özellikleri: " + str(pacmanResmi.shape)) # genişlik,yükseklik,renk kanalı
print("Resmin Veri Tipi: " + str(pacmanResmi.dtype))




cv2.waitKey(0)
cv2.destroyAllWindows()