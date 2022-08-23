import cv2
import numpy as np

yasam=cv2.imread("ResimGrilestirme\dunya.jpg")

yasamGri=cv2.cvtColor(yasam,cv2.COLOR_BGR2GRAY)

yukseklik,genislik,kanalSayisi = yasam.shape
print("Orijinal",yukseklik,genislik,kanalSayisi )

yukseklik,genislik = yasamGri.shape
print("Gri_resim",yukseklik,genislik)
#Resmi grileştirdiğimde kanal sayısı bire düşer..

cv2.imshow("Dunya",yasam)
cv2.imshow("Gri_resim",yasamGri)

cv2.waitKey(0)
cv2.destroyAllWindows()