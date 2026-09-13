import cv2
img = cv2.imread("input1.jpg", 0)
equalized = cv2.equalizeHist(img)
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equalized)
cv2.imwrite("output.png", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
