import numpy as np
import cv2

img=cv2.imread("img.jpg",0)
cv2.imshow("Desktop",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("gray1.jpg",img)
