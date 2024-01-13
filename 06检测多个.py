import cv2 as cv

#绘制函数
def face_detect_demo():
    pary = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # 加载分类器
    face_detect = cv.CascadeClassifier(
        "D:/openvc/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml")
    face = face_detect.detectMultiScale(pary,1.1,5,0,(5,5),(100,100))  # detectMultiScale返回脸部的矩形x, y, w, h
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('face',img)

# 读取图片
img = cv.imread("img/img_4.png")
# 检测函数
face_detect_demo()
while True:
    if ord("q") == cv.waitKey(0):
        break
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyWindow()
