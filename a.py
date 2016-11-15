import numpy as np                          #latest versions of numpy and openCV2
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()                 #the frames captured here,this 'frame' to be sent via sockets


    cv2.imshow('frame',frame)               #this is what generates the output screen,used at the receiver's end
    if cv2.waitKey(1) & 0xFF == ord('q'):   #stops the endless loop when 'q' is pressed
        break

cap.release()                               #releases the feed(zaruri hai krna)
cv2.destroyAllWindows()