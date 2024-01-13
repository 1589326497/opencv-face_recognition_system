import cv2 as cv

# 获取图片
img = cv.imread("img/img_1.png")
# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示修改后的
cv.imshow("resize_img", resize_img)
# 打印原图尺寸的大小
print("原图尺寸", img.size)
# 打印修改后的大小
print("打印修改", resize_img.size)
# 等待
while True:
    if ord("q")==cv.waitKey(0):
        break
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyWindow()
