# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
调用Windows系统通知功能
"""

from win10toast import ToastNotifier
import time

print("notification")

def notice_tensor():
    toaster = ToastNotifier()
    toaster.show_toast("训练中", "正在通过TensorFlow训练导入的模型，请耐心等待")
    # 在5秒后消失
    time.sleep(5)
    toaster.hide_toast()

def notice_video():
    toaster = ToastNotifier()
    toaster.show_toast("渲染中", "正在渲染多路视频，出现未响应为正常现象，请耐心等待")

def notice_detector():
    toaster = ToastNotifier()
    toaster.show_toast("识别器", "已成功加载视频源与数据集，若要退出请点击ESC键")

def welcome():
    toaster = ToastNotifier()
    toaster.show_toast("欢迎", "欢迎使用基于机器学习的行人识别系统")

def notice_video_complete():
    toaster = ToastNotifier()
    toaster.show_toast("视频合成器", "已完成视频渲染")

def notice_developer():
    toaster = ToastNotifier()
    toaster.show_toast("制作者信息", "北方工业大学\n计 19-3\n钱晟\n")

