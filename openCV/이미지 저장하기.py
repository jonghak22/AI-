import cv2

img = cv2.imread("./images/lena.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("lenagray.png",img)