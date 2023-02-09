import cv2
import numpy as np
from datetime import datetime
def mouseHandler(event, x, y, flag, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print(event, x, y)
        print(datetime.today())
        filename = str(datetime.today().microsecond)+".jpg"
        cv2.imwrite(filename, img)
cv2.namedWindow("Movie")
cv2.setMouseCallback("Movie", mouseHandler)
cap = cv2.VideoCapture("./images/Puppies-HD.mp4")
img = None
if cap.isOpened :
    print(cap.get(cv2.CAP_PROP_FPS))
    delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))
    while True :
        ret, img = cap.read()
        if ret:
            cv2.imshow("Movie", img)
            if cv2.waitKey(delay) & 0xFF == 27 : # esc키 입력시
                print("ESC Key Pressed")
                break
        else :
            print("No Frame")
            print(ret, img)
            break
else :
    print("File Not Opened")
cap.release()
cv2.destroyAllWindows()