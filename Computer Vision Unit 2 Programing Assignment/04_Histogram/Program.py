import cv2
import numpy as np
img = cv2.imread("input.jpg", 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = hist.ravel()
max_intensity = np.argmax(hist)
print("Intensity with highest frequency:", max_intensity)
print("Highest frequency:", int(hist[max_intensity]))
hist_img = np.zeros((400, 512), dtype=np.uint8)
hist_norm = cv2.normalize(hist, None, 0, 400, cv2.NORM_MINMAX)
for i in range(256):
    x = i * 2
    cv2.line(hist_img, (x, 400), (x, 400 - int(hist_norm[i])), 255, 1)
cv2.imwrite("output.png", hist_img)
cv2.imshow("Histogram", hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
