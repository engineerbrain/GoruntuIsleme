# Resim Açma Okuma Yazma

import cv2
import numpy as np

resim = cv2.imread("bmw.png",0) #yöntem, belirtilen dosyadan bir görüntü yükler.. İkinci parametre rengi belirler..

cv2.imshow("Fatch",resim)

cv2.imwrite("bmwgriresim.png",resim)# ana resmin kopyası gibi düşün..

# Temek iskeletlerim..

cv2.waitKey(0) # Kapanıştaki temel iskelet. Pencere açıldığında ekranın kalması için herhangi bir yere basmamızı sağlar.
cv2.destroyAllWindows() # çarpıya bastığımızda opencv ile ilgili tüm pencerelerin kapanmasını sağlar

