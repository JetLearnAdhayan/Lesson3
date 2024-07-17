import cv2

image1 = cv2.imread("pika.png")

cv2.imshow("orignal", image1)
gray_image=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

cv2.imshow("grey_scale",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

