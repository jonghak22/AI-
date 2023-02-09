from IPython.display import display, HTML
display(HTML("<style>div.container { width:100% !important; }</style>"))

#1.2 opencv

import cv2
print(cv2.__version__)

#1.2.2 이미지 불러오기

lena_img = cv2.imread(".images/lena.jpg",cv2.IMREAD_GRAYSCALE)
lena_img

type(lena_img)

