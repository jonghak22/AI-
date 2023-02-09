import cv2
import matplotlib.py plot as plt
%matplotlib inline
img = cv2.imread("./images/lena.jpg", cv2.IMREAD_COLOR)
plt.imshow(img)
plt.show()