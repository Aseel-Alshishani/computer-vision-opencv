import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    colors = {
        'Green': ((40,50,50), (80,255,255)),
        'Orange': ((10,100,100),(25,255,255)),
        'Blue': ((100,150,0),(140,255,255))        
    }
    
    color_name = 'Unknown'
    for name ,(lower , upper) in colors.items():
        lower = np.array(lower)
        upper = np.array(upper)
        mask =cv2.inRange(hsv,lower , upper)
        if cv2.countNonZero(mask)>500:
            color_name= name
            break
        
    cv2.putText(frame,color_name, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5 , (255,255,255) ,3 )
    
    cv2.imshow('Color Detection',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()