import cv2 as cv

# 获取图片
img = cv.imread("img/img_1.png")
# 坐标
x, y, w, h = 100, 100, 100, 100
# 绘制矩形
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)
# 绘制圆形
cv.circle(img, center=(x + w, y + h), radius=100, color=(255, 0, 0), thickness=5)
# 显示
cv.imshow('img',img)
# 等待
while True:
    if ord("q") == cv.waitKey(0):
        break
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyWindow()
