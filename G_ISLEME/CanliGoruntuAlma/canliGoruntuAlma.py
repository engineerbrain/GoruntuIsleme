import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.imshow("goruntu",goruntu)

    if cv2.waitKey(30) & 0xFF ==('q'):
        break

kamera.release()

cv2.destroyAllWindows()
