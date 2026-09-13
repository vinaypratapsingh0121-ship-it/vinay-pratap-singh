import cv2
import numpy as np
img = cv2.imread("input2.jpg", 0)
smooth = cv2.GaussianBlur(img, (5, 5), 0)
Kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2. filter2D(smooth, -1,  Kernel)
cv2.imshow("output.png", img)
cv2.imshow("Smoothing", smooth)
cv2.imshow("output_smooth.png", smooth)
cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)
cv2.waitKey(0)
cv2.destroyAllWindow()
