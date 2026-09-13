import cv2
img = cv2.imread("input.jpg", 0)
mean = cv2.blur(img, (5, 4))
cv2.imshow("Original Image", img)
cv2.imshow("Mean Image", mean)
cv2.imwrite("output.png", mean)
cv2.waitKey(0)
cv2.destroyAllWindows()
