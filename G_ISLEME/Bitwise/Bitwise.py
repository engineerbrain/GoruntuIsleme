import cv2
import numpy as np

image1= cv2.imread("G_ISLEME\Bitwise\daire.png")
image2= cv2.imread("G_ISLEME\Bitwise\siyah_beyaz.png")

bit_And=cv2.bitwise_and(image1,image2)
bit_Or=cv2.bitwise_or(image1,image2)
bit_Not=cv2.bitwise_not(image1)
bit_Not2=cv2.bitwise_not(image2)
bit_Xor=cv2.bitwise_xor(image1,image2)








cv2.imshow("ilk resim",image1)
cv2.imshow("ikinci resim",image2)
cv2.imshow("bit_And",bit_And)
cv2.imshow("bit_Or",bit_Or)
cv2.imshow("bit_Not",bit_Not)
cv2.imshow("bit_Not2",bit_Not2)
cv2.imshow("bit_Xor",bit_Xor)








cv2.waitKey(0)
cv2.destroyAllWindows()