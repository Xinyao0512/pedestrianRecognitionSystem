# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
检测器部分，实现图像识别功能
摄像头实时视频分析
通过视频合成模块进行多路图像处理
"""

import cv2
import time
import psutil
import subprocess
from tkinter import messagebox

print("detectorlite")

#导入私有库
import performance
import notification

# 机器学习函数
# 功能正在开发
def MachineLearing(TensorPath):
    # 机器学习模块通知
    # performance.performance_test()
    return 0

def detector(XMLPath,localPath,TensorPath,a):
    # 主函数显示识别结果
    # 后台展示执行结果
    if a == 0:
        print(f"传递的文件路径为：{localPath}")
        print(f"传递的数据集路径为：{XMLPath}")
    elif a == 1:
        print("从摄像头读取视频")
        print(f"传递的数据集路径为：{XMLPath}")
    elif a == 2:
        print("从文件训练模型")
        print(f"传递的数据集路径为：{TensorPath}")
        MachineLearing(TensorPath)
    elif a == 3:
        print("视频成功合成")
        print(f"合成后的视频路径为：{localPath}\output.mp4")
        a = 0

    # 创建一个窗口来显示视频流
    cv2.namedWindow("Detecting")
    cv2.resizeWindow("Detecting", 1280, 720)

    # 加载人脸和行人检测分类器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
    XMLModel_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + XMLPath)
    # XMLModel_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "D:\model\model.h5")
    # 使用摄像头捕获视频流
    if a == 0:
        cap = cv2.VideoCapture(localPath)  # 'D:\System folder\Desktop\1.mp4'
    elif a == 1:
        cap = cv2.VideoCapture(0)
    else:
        exit(0)

    # 识别器通知
    notification.notice_detector()

    # 获取视频帧的宽度和高度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 指定显示帧的尺寸
    window_width = 1280
    window_height = 720

    # 计算缩放比例
    scale = min(window_width / width, window_height / height)

    # 计算缩放后的尺寸
    display_width = int(width * scale)
    display_height = int(height * scale)

    # 新建计数器
    frame_count = 0
    start_time = time.time()

    # 循环读取视频流中的帧
    while True:

        # 读取视频帧
        ret, frame = cap.read()

        # 异常处理
        if not ret:
            print("无法连接摄像头/未找到文件")
            break

        # 将帧转换为灰度图像，因为人脸和行人检测需要灰度图像作为输入
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 对灰度图像进行人脸检测
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        # 对灰度图像进行行人检测
        pedestrians = pedestrian_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                          flags=cv2.CASCADE_SCALE_IMAGE)

        if XMLPath:
            # 对灰度图像进行导入模型检测
            XMLModel = XMLModel_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                         flags=cv2.CASCADE_SCALE_IMAGE)

        # 在每个检测到的人脸周围绘制矩形框，并在框内标注"face"
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 在每个检测到的行人周围绘制矩形框，并在框内标注"pedestrian"
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "pedestrian", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if XMLPath:
            # 在每个检测到的行导入模型周围绘制矩形框，并在框内标注"XMLModel"
            for (x, y, w, h) in XMLModel:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, "XML_Model", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # 帧数加1
        frame_count += 1

        # 计算帧率并显示
        # if frame_count % 10 == 0:
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time
        cv2.putText(frame, "FPS: {:.2f}".format(fps), (3, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # 获取 CPU 使用率
        cpu_percent = psutil.cpu_percent()

        # 打印 CPU 使用率
        cv2.putText(frame, "CPU: {:.2f} %".format(cpu_percent), (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # 执行 nvidia-smi 命令获取 GPU 占用情况
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv'])

        # 将输出转换为字符串，并获取 GPU 占用率
        gpu_percent = int(output.decode().split('\n')[1].strip().replace('%', ''))

        # 打印 GPU 占用率
        cv2.putText(frame, "GPU: {:.2f} %".format(gpu_percent), (3, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # 获取系统内存使用情况
        mem = psutil.virtual_memory()

        # 获取剩余内存大小，单位为 GB
        free_mem = mem.available / 1024 / 1024 / 1024

        # 打印剩余内存大小
        cv2.putText(frame, "MEM: {:.2f} GB".format(free_mem), (3, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # 缩放视频帧的尺寸
        frame = cv2.resize(frame, (display_width, display_height))

        # 显示处理后的帧
        cv2.imshow("Detecting", frame)

        # 按下ESC键退出程序
        if cv2.waitKey(1) == 27:
            break

    # 释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()

"""
导入必要的库，包括OpenCV、time、psutil、subprocess和tkinter等。
定义了一个机器学习函数MachineLearning(TensorPath)，但该功能目前还在开发中，返回值为0。
定义了一个主函数detector(XMLPath, localPath, TensorPath, a)，其中a表示程序的运行模式：0表示从本地文件读取视频，1表示从摄像头读取视频，2表示从文件训练模型，3表示视频成功合成。
在主函数中创建一个窗口来显示视频流，并加载人脸和行人检测的分类器。
根据传递进来的参数a，选择从本地文件或摄像头读取视频。
循环读取视频流中的帧，将每一帧图像转换为灰度图像，并在灰度图像上进行人脸和行人检测。
如果传递进来的XMLPath参数不为空，则导入模型文件并进行模型检测。
在每个检测到的人脸周围绘制矩形框，并在框内标注"face"，在每个检测到的行人周围绘制矩形框，并在框内标注"pedestrian"。
最后，将处理后的帧显示在窗口中，并在控制台输出相关信息。
"""