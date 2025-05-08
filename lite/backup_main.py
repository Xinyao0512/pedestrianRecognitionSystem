# © Copyright 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
主程序部分，显示主界面
支持视频文件输入(含云端文件)，多路视频监控
自定义数据集与模型调用
摄像头实时视频分析
通过视频合成模块进行多路图像处理
"""

import sys
sys.path.append("..")
from tkinter import *
from PIL import Image, ImageTk
from logging import root
from tkinter import messagebox

#导入私有库
import Video_Post
# import advancedDetector
import notification
import detectorlite
import error
import login
import tfm
import test

# 登录认证
verification = login.sys_login()
if verification != 2:
    notification.notice_developer()
    exit(0)

# 创建主窗口
root = Tk()
root.title("北方工业大学")
root.geometry("1280x720")
root.resizable(False, False)

# 设置窗口图标
root.iconbitmap("./img/ncut.ico")

# 加载背景图像
bg_image = Image.open("./img/index.png")
bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 设置输入框样式
entry_style = {"background": "#f0f5ff", "highlightthickness": 0, "border": 0}

# 创建输入框
video_entry = Entry(root, width=70, **entry_style)
video_entry.place(relx=0.575, rely=0.285, anchor=NW)

dataset_entry = Entry(root, width=70, **entry_style)
dataset_entry.place(relx=0.575, rely=0.395, anchor=NW)

ml_entry = Entry(root, width=70, **entry_style)
ml_entry.place(relx=0.575, rely=0.51, anchor=NW)

# 设置字体
button_font = {"size": 20, "weight": "bold"}

# 创建按钮
single_btn = Button(root, text="单路监控", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
single_btn.place(relx=0.59, rely=0.62, anchor=NW)

multi_btn = Button(root, text="多路监控", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
multi_btn.place(relx=0.782, rely=0.62, anchor=NW)

ml_btn = Button(root, text="模型训练", width=55, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
ml_btn.place(relx=0.587, rely=0.81, anchor=NW)

ml_advanced = Button(root, text="高级识别", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
ml_advanced.place(relx=0.59, rely=0.715, anchor=NW)

ml_exitprogram = Button(root, text="退出程序", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
ml_exitprogram.place(relx=0.782, rely=0.715, anchor=NW)


# 定义按钮响应函数
def local():
    root.withdraw()
    global localPath, XMLPath, a, TensorPath
    a = 0
    localPath = video_entry.get()
    XMLPath = dataset_entry.get()
    TensorPath = ml_entry.get()
    if not XMLPath:
        print("调用默认XML数据集")
        XMLPath = "haarcascade_upperbody.xml"
    if not localPath:
        a = 1
    if localPath and error.video_check(localPath):
        messagebox.showwarning("警告", f"文件格式错误")
        root.deiconify()
        return 0

    # 进入图像识别
    detectorlite.detector(XMLPath, localPath, TensorPath, a)
    root.deiconify()
    print("单路监控：视频源：", localPath, "，数据集模型输入源：", XMLPath)

def combine():
    root.withdraw()
    global localPath, TensorPath, XMLPath, a
    localPath = video_entry.get()
    XMLPath = dataset_entry.get()
    TensorPath = ml_entry.get()
    a = 3
    if not XMLPath:
        print("调用默认XML数据集")
        XMLPath = "haarcascade_upperbody.xml"

        # 检测mp4数量
    if error.mp4_count(localPath):
        # 显示窗口
        root.deiconify()
        return 0
    messagebox.showinfo("提示",
                        f"多路识别目前仅支持录像识别\n视频源路径为：{localPath}\n识别默认为四路2k视频流\n合成结束后自动开始识别")
    print(f"传递的视频文件夹路径为：{localPath}")
    Video_Post.combiner(localPath)
    localPath = localPath + "\\output.mp4"
    print(localPath)

    # 进入图像识别
    detectorlite.detector(XMLPath, localPath, TensorPath, a)

    # 显示窗口
    root.deiconify()
    print("多路监控：视频源：", localPath, "，数据集模型输入源：", XMLPath)

#退出程序
def exitprogram():
    exit(0)

#机器学习模块
def tensor():
    global TensorPath, a
    a = 2
    TensorPath = ml_entry.get()
    p = 1
    root.withdraw()
    if TensorPath:
        tfm.machineLearning(TensorPath, TensorPath, p)
        root.deiconify()
    else:
        messagebox.showwarning("警告", f"文件路径不能为空")
        root.deiconify()
    print("机器学习：机器学习文件源：", TensorPath)

"""
#高级识别功能
def yolo_advanced():
    exit(0)

"""

#高级识别功能
def yolo_advanced():
    root.withdraw()
    # messagebox.showinfo("提示",
    #                     f"高级功能可提供GPU加速\n更高的图像识别率\n支持YOLOv5与PyTorch功能")
    # global localPath, TensorPath, XMLPath, a
    # localPath = video_entry.get()
    # XMLPath = dataset_entry.get()
    # TensorPath = ml_entry.get()
    # if not localPath:
    #     a = 5
    # else:
    #     a = 6
    # advancedDetector.advancedPro(localPath, a)
    root.deiconify()


# 绑定按钮响应函数
single_btn.config(command=local)
multi_btn.config(command=combine)
ml_btn.config(command=tensor)
# ml_advanced.config(command=yolo_advanced)
ml_exitprogram.config(command=exitprogram)

# 运行主循环
root.mainloop()
