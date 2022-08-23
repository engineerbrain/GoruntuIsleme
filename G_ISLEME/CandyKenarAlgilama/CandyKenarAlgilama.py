import cv2
import numpy as np

image= cv2.imread("G_ISLEME\CandyKenarAlgilama\image.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blu=cv2.GaussianBlur(gray,(3,3),0)


#canny=cv2.Canny(blu,50,150)

def autoCanny(blu,sigma=0.33):
    median=np.median(blu)
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0+sigma)*median))
    canny=cv2.Canny(blu,lower,upper)
    
    return canny

wide=cv2.Canny(blu,10,220) #geniş
tight=cv2.Canny(blu,200,300) #dar
auto=autoCanny(blu)




# cv2.imshow("orijinal",image)
# cv2.imshow("gray",gray)
#cv2.imshow("canny",canny) # orijinal resmindeki kenarları algılıyor..

# cv2.imshow("wide",wide)
# cv2.imshow("tightl",tight)
# cv2.imshow("auto",auto)

cv2.imshow("edges(kenarlar)",np.hstack([blu,wide,tight,auto])) # çıktıları yan yana sıralar



cv2.waitKey(0)
cv2.destroyAllWindows()