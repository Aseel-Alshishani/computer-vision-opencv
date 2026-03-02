import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    inverted =cv2.bitwise_not(frame)

    cv2.imshow('Camera', frame )
    cv2.imshow('Gray', gray )
    cv2.imshow('Inverted Colors', inverted )


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

