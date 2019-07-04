import cv2
img = cv2.imread("sonic.png", 0)
cv2.imshow('sonic', img)
cv2.waitKey(0)
img2 = cv2.imread("sonic.png", 7)
cv2.imshow('sonic', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()