import cv2
import numpy as np

resim1 = cv2.imread("AGIRLIKLARITOPLAMA2\resim1.jpg")
resim2 = cv2.imread("AGIRLIKLARITOPLAMA2\resim2.jpg")


cv2.imshow("resim1",resim1)
cv2.imshow("resim2",resim2)

toplam=cv2.add(resim1,resim2)
agirlikliToplama=cv2.addWeighted(resim1,0.7,resim2,0.3,0)

cv2.imshow("Toplanmıs_resimler",toplam)
cv2.imshow("Ağırlıklı Toplama",agirlikliToplama)


cv2.waitKey(0)
cv2.destroyAllWindows()