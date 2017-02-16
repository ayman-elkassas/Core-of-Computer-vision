import numpy as np
import cv2
#for output
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.mp4",fourcc, 20.0, (640,480))
#start capture
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #to flip camera

    # frame = cv2.flip(frame, 0)

    #convert from BGR 2 GRAY
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display
    cv2.imshow("Capture",gray)
    #write in output and prepare it
    out.write(frame)
    k=cv2.waitKey(1)
    if k==ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()









