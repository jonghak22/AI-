# import cv2
# cap = cv2.VideoCapture("./images/Puppies-HD.mp4")
# if cap.isOpened() :
#     delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))
#     while True :
#         ret, img = cap.read()
#         if ret:
#             cv2.imshow("Movie", img)
#             if cv2.waitKey(delay) & 0xFF == 27 : # esc키 입력시
#                 print("ESC Key Pressed")
#                 break
#         else :
#             print("No Frame")
#             print(ret, img)
#             break
# else :
#     print("File Not Opend")
# cap.release()
# cv2.destroyAllWindows()

import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened() :
    delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))
    while True :
        ret, img = cap.read()
        if ret:
            cv2.imshow("Movie", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
            if cv2.waitKey(delay) & 0xFF == 27 : # esc키 입력시
                print("ESC Key Pressed")
                break
        else :
            print("No Frame")
            print(ret, img)
            break
else :
    print("Camera Not Opend")