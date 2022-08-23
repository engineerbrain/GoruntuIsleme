import cv2
import numpy as np

joker = cv2.imread("joker.jpg")
# joker[:,:,0]=50 #mavi
# joker[:,:,1]=50 # yeşil
# joker[:,:,2]=0  # kırmızı

joker[55:80,90:150,0] = 255 # y,x,bgr
joker[55:80,90:150,1] = 200

cv2.imshow("joker",joker)



cv2.waitKey(0)
cv2.destroyAllWindows()