import numpy as np
import cv2
import random

ran=random.randrange(0,255,1)
img=np.zeros((512,512,3),np.int8)

cv2.line(img,(0,0),(511,511),(ran,0,0),50)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

