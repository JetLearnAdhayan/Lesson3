import cv2

image1 = cv2.imread("pika.png")

cv2.imshow("orignal", image1)

edge_detection=cv2.Canny(image1,50,250)

#t_lower = 50 #lower threshold
#t_upper = 250 #Upper threshold

cv2.imshow("detection", edge_detection)





cv2.waitKey(0)
cv2.destroyAllWindows()