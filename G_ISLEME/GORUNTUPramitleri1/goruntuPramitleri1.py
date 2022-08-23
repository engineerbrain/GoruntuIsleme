import cv2
import numpy as np

kaplan = cv2.imread("GORUNTUPramitleri1\kaplan.jpg")

ikiKatBuyuk = cv2.pyrUp(kaplan)

ikiKatKucuk = cv2.pyrDown(kaplan)

print("Orijinal", kaplan.shape)

print("Iki kat buyuk resim",ikiKatBuyuk.shape)

print("Iki kat kucuk resim",ikiKatKucuk.shape)



cv2.imshow("Orijinal resim",kaplan)
cv2.imshow("Iki kat buyuk resim",ikiKatBuyuk)
cv2.imshow("Iki kat kucuk resim",ikiKatKucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()