import cv2
import numpy as np

ayi = cv2.imread("BolgeAlma\ayi.jpg")

kesit=ayi[50:150,300:400]

ayi[0:100,0:100] = kesit

ayi[ : ,: ,2]=255

cv2.imshow("kesit alanı",kesit)
cv2.imshow("Ayı",ayi)

cv2.waitKey(0)
cv2.destroyAllWindows()