import cv2
import numpy as np



kedi = cv2.imread("Bolge\cat.jpg")


kedi = cv2.rectangle(kedi, (50,30),(100,70), [0,255,0],1)

cv2.imshow("Kedi",kedi)


cv2.waitKey(0)
cv2.destroyAllWindows()
