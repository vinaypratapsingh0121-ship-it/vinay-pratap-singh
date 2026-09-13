import cv2
import numpy as np
img = cv2.imread("input2.jpg")
brightness = np.ones(img.shape, dtype=np.uint8) * 50
bright_img = cv2.add(img, brightness)
print("Before", img[110, 110])
print("After", bright_img[110, 110])
cv2.imshow("Original", img)
cv2.imshow("Bright image", bright_img)
cv2.imwrite("output.png", bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
