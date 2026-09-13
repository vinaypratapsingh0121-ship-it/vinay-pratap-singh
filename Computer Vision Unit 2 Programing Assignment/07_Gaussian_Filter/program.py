import cv2
img = cv2.imread("input3.jpg", 0)
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imwrite("output.png", gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
