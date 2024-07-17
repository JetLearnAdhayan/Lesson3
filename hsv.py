import cv2


image1 = cv2.imread("pika.png")

cv2.imshow("orignal", image1)

HSV_IMAGE = cv2.cvtColor(image1, cv2.COLOR_RGB2HSV)

cv2.imshow("HSV_Image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
