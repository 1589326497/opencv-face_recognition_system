import cv2 as cv

# 获取图片
img = cv.imread("img/img_1.png")
# 显示图片
cv.imshow('read_img',img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyWindow()
