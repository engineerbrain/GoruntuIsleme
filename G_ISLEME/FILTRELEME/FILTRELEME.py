from email.mime import image
import cv2
import numpy as np

image = cv2.imread("G_ISLEME\FILTRELEME\hard.jpg")

# matrisin ortalaması alınır ve orta kısma yazılır
meanFilter=cv2.blur(image,(3,3))
meanFilter2=cv2.blur(image,(5,5))


cv2.imshow("Orijinal",image)
cv2.imshow("mean Filter",meanFilter)
cv2.imshow("mean Filter2",meanFilter2)

# matrisin pikseleri sıralanır ortadaki değerin pikseli ele alınır.

medianFilter=cv2.medianBlur(image,3)

medianFilter2=cv2.medianBlur(image,5)

medianFilter3=cv2.medianBlur(image,7) # resmin orijinalliği gidiyor


cv2.imshow("median Filter",medianFilter)

cv2.imshow("median Filter2",medianFilter2)

cv2.imshow("median Filter3",medianFilter3)

# piksellerin ağırlık ortalamalarını çıkartıyor # daha avantajlı

gauss=cv2.GaussianBlur(image,(3,3),0)

gauss2=cv2.GaussianBlur(image,(5,5),0)

gauss3=cv2.GaussianBlur(image,(7,7),0)


cv2.imshow("gauss Filter",gauss)

cv2.imshow("gauss Filter2",gauss2)

cv2.imshow("gauss Filter3",gauss3)




cv2.waitKey(0)
cv2.destroyAllWindows()