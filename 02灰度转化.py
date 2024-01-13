import cv2 as cv

# 获取图片
img = cv.imread("img/img_1.png")
#灰度转化
gray_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#显示灰度
cv.imshow('gray_img',gray_img)
#保存灰度图片
cv.imwrite('img/gray_img.jpg',gray_img)
# 显示图片
cv.imshow('read_img',img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyWindow()
