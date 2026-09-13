import cv2
import numpy as np
img = cv2.imread("input1.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
crows, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.uint8)
r = 30
mask[crows-r: crows+r, ccol-r: ccol+r] = 1
filtered_dft = dft_shift*mask
inverse_dft = np.fft.ifftshift(filtered_dft)
img_back = cv2.idft(inverse_dft)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
img_back = (np.uint8)(img_back)
cv2.imshow("output.png", img)
cv2.imshow("LPH", img_back)
cv2.imwrite("output.png", img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
