# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture(0)
# while(True):
#     # 一帧一帧捕捉
#     ret, frame = cap.read()
#     # 我们对帧的操作在这里
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # 显示返回的每帧
#     cv.imshow('frame',gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# # 当所有事完成，释放 VideoCapture 对象
# cap.release()
# cv.destroyAllWindows()

import cv2 as cv
import numpy as np
#加载两张图片
cv.namedWindow("res", cv.WINDOW_NORMAL)
img1 = cv.imread('./data/messi5.jpg')
img2 = cv.imread('./data/opencv-logo.png')
# print(img2.shape)
# #img2 = img2[0:187,0:150]
# cv.imshow('res',img2)
# cv.waitKey(0)
# cv.destroyAllWindows()

#我想在左上角放置一个logo，所以我创建了一个 ROI,并且这个ROI的宽和高为我想放置的logo的宽和高
rows,cols,channels = img2.shape
print(type(img2.shape))
roi = img1 [0:rows,0:cols]
#现在创建一个logo的掩码，通过对logo图像进行阈值，并对阈值结果并创建其反转掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

cv.imshow('img2gray',img2gray)
cv.waitKey(0)
cv.destroyAllWindows()

ret,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
#现在使 ROI 中的徽标区域变黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
#仅从徽标图像中获取徽标区域。
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
#在 ROI 中放置徽标并修改主图像
dst = cv.add(img1_bg,img2_fg)
img1 [0:rows,0:cols] = dst
print(cv.__version__)
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
