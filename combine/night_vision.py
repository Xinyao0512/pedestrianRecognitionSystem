import os
import cv2
import numpy as np

def simulate_infrared_video(video_path):
    # 读取视频
    cap = cv2.VideoCapture(video_path)

    # 获取视频信息
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 创建视频编写器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_path = os.path.join(os.path.dirname(video_path), 'IR.mp4')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 循环读取视频帧
    while True:
        ret, frame = cap.read()

        # 判断是否读取到帧
        if not ret:
            break

        # 将彩色图像转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 应用伪彩色映射
        ir_gray = cv2.applyColorMap(gray, cv2.COLORMAP_HOT)

        # 将灰度图像转换为彩色图像
        ir = cv2.cvtColor(ir_gray, cv2.COLOR_BGR2RGB)

        # 写入输出视频
        out.write(ir)

    # 释放资源
    cap.release()
    out.release()

    # 返回输出视频的路径
    return output_path


def temp_video(input_path):
    # 打开输入视频
    cap = cv2.VideoCapture(input_path)

    # 获取视频的基本信息
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建输出视频的编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_path = os.path.join(os.path.dirname(input_path), 'temp.mp4')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # 处理每一帧
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 将帧转换成灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 应用热感应滤波器
        filtered = cv2.applyColorMap(gray, cv2.COLORMAP_HOT)

        # 将处理后的帧写入输出视频
        out.write(filtered)

    # 释放资源
    cap.release()
    out.release()

    return output_path
