
import cv2 
import matplotlib.pyplot as plt



img = cv2.imread("./images/lena.jpg",cv2.IMREAD_COLOR)


plt.imshow(img)
plt.show