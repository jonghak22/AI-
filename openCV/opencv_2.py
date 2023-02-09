import cv2

fname = "./images/lena.jpg"

color = cv2.imread(fname,cv2.IMREAD_COLOR)
grayscale = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
unchanged = cv2.imread(fname,cv2.IMREAD_UNCHANGED)

cv2.imshow("Color",color)
cv2.imshow("Grayscale",grayscale)
cv2.imshow("Unchanged",unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows