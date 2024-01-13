import os
import cv2
from PIL import Image
import numpy


def getImageAndLabels(path):
    # 存储人脸数据
    facesSamples = []
    # 存储姓名数据
    ids = []
    # 存储图像信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类器
    face_detect = cv2.CascadeClassifier(
        "Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml")
    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片，灰度化 PIL 有九种不同的模式：1，L，P，RGB，RGBA，CMYK，YCbCr，I，F
        PIL_img = Image.open(imagePath).convert('L')
        # 将图片转化为数组，以黑白深浅
        img_numpy = numpy.array(PIL_img, 'uint8')
        # 获取图片人脸特征
        faces = face_detect.detectMultiScale(img_numpy)
        # 获取每张图片的ID和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        # 预防无面容照片
        for x, y, w, h in faces:  # 遍历人脸列表中的每个元素
            # 提取人脸区域并存储到facesSamples列表中
            ids.append(id)
            # 将对应的标识符添加到ids列表中
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            # 打印脸部特征和id
            print('id', id)
    print('fs:', facesSamples)
    # print('脸部例子：',facesSamples[0])
    # print('身份信息：',ids[0])
    return facesSamples, ids


if __name__ == '__main__':
    # 图片路径
    path = 'data/'
    # 获取图像数组和id标签数组和姓名
    faces,ids = getImageAndLabels(path)
    # 加载识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 训练
    recognizer.train(faces, numpy.array(ids))
    # 保存文件
    recognizer.write("trainer/trainer.yml")
