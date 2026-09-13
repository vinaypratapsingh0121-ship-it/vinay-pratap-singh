import cv2
import numpy as np
img = cv2.imread("input1.jpg")
minimum = np.min(img)
maximum = np.max(img)
strech = (img-minimum)*(255.0/(maximum-minimum))
strech = strech.astype(np.uint)
cv2.imshow("output.png", img)
cv2.imshow("strech", strech)
cv2.imwrite("output.png", strech)
cv2.waitKey(0)
cv2.destroyAllWindows()
