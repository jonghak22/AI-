import cv2

cap = cv2.VideoCapture("./images/Puppies-HD.mp4")

if cap.isOpened:
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width),int(height))
    fps = cap.get(cv2.CAP_PROP_FPS)


    out = cv2.VideoWriter("video.avi",fourcc,fps,size)

    print(cap.get(cv2.CAP_PROP_FPS))
    delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))
    print(width,height,size,fps,delay)

    while True:
        ret,img = cap.read()
        if ret:
            gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            cv2.imshow("Movie",gray)
            out.write(cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR))
            if cv2.waitKey(delay) & 0XFF ==27:
                print("윈도우 종료")
                break
        
        else:
            print("No frame")
            print(ret,img)
            break
else:
    print("비디오 안열림")

cap.release()
cv2.destroyAllWindows()