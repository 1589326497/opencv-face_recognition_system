import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)
name = 'MoKunHua'
falg = 1
num = 1
while (cap.isOpened()):  # 检测摄像头是否打开
    ret_flag, Vshow = cap.read()
    cv2.imshow("Capture_Text", Vshow)  # 显示图像
    k = cv2.waitKey(1) & 0xFF  # 按键判断 (1)是等待1毫秒 0xFF操作是为了将结果转换为无符号整数
    if k == ord(' '):
        cv2.imwrite("data\\" + str(num) + "." + name + ".jpg", Vshow)
        print("已保存 " + str(num) + name + ".jpg")
        print("--------------")
        num += 1
    elif k == ord('e'):  # 按下e退出
        break

# 关闭摄像头 释放内存
cap.release()
cv2.destroyWindow()
