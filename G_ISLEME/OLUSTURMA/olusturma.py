import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(20,60,255),3) #atadığım resim,başlangıç noktası,aralık,renk,kalınlık

cv2.circle(resim,(150,150),25,(0,255,0),2) #atadığım resim,başlangıç noktası,çap,renk,kalınlık

cv2.putText(resim,"FATMA",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow("deneme",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()