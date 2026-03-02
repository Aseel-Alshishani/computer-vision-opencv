import cv2
import numpy as np

img = np.zeros((500,800,3) , dtype = np.uint8 )

cv2.putText(img ,'Welcome to OpenCV!', (50,100) , cv2.FONT_HERSHEY_SIMPLEX ,2 , (255,0,255) , 3 )
cv2.putText(img , 'Aseel Ersnoy' , (50,200) , cv2.FONT_HERSHEY_COMPLEX , 1.5 , (255,0,255) ,2 )
cv2.putText(img , '2026',( 50 , 300 ) , cv2.FONT_HERSHEY_DUPLEX , 1.8 , (255,0,255) ,2 )

cv2.rectangle(img , (40,350), (400,450) ,(255, 255, 0) ,3)

cv2.imshow('Text on Image' , img )
cv2.waitKey(0)
cv2.destroyAllWindows()