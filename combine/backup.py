# Copyright © 2023 Sheng Qian. All rights reserved.
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

from tkinter import *
from PIL import Image, ImageTk
from logging import root
from tkinter import messagebox
import subprocess
import requests
import webbrowser
import urllib.request

#导入私有库
import Video_Post
import advancedDetector
import notification
import detectorlite
import error
import login
import tfm
import server
import blackwhite
import eggs
import test

def main():

    print("main")

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
    video_entry.place(relx=0.576, rely=0.285, anchor=NW)

    dataset_entry = Entry(root, width=70, **entry_style)
    dataset_entry.place(relx=0.576, rely=0.397, anchor=NW)

    ml_entry = Entry(root, width=70, **entry_style)
    ml_entry.place(relx=0.576, rely=0.51, anchor=NW)

    # 设置字体
    button_font = {"size": 20, "weight": "bold"}
    version_font = {"size": 10, "weight": "bold"}

    # 创建按钮
    single_btn = Button(root, text="基础识别", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    single_btn.place(relx=0.59, rely=0.625, anchor=NW)

    multi_btn = Button(root, text="合成并识别", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    multi_btn.place(relx=0.782, rely=0.623, anchor=NW)

    ml_btn = Button(root, text="本地训练", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    ml_btn.place(relx=0.592, rely=0.82, anchor=NW)

    ml_advanced = Button(root, text="高级识别", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    ml_advanced.place(relx=0.59, rely=0.715, anchor=NW)

    blackwhiteb = Button(root, text="图像处理", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    blackwhiteb.place(relx=0.782, rely=0.715, anchor=NW)

    ml_server = Button(root, text="云端训练", width=23, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    ml_server.place(relx=0.782, rely=0.82, anchor=NW)

    eggsv = Button(root, text="ver 1.19.511", width=15, height=1 , highlightthickness=0, bd=0, bg="white", fg="black", activebackground="white", font=button_font)
    eggsv.place(relx=0.91, rely=0.965, anchor=NW)

    update = Button(root, text="版本更新", width=10, height=1, highlightthickness=0, bd=0, bg="white", fg="black",
                   activebackground="white", font=button_font)
    update.place(relx=0.535, rely=0.965, anchor=NW)

    ml_exitprogram = Button(root, text="帮助", width=10, height=1, highlightthickness=0, bd=0, bg="white", fg="black",
                    activebackground="white", font=button_font)
    ml_exitprogram.place(relx=0.95, rely=0.005, anchor=NW)

    def upper():
        url = "http://cmccprivatecloud.dynv6.net:9001/update.txt"
        try:
            response = requests.head(url)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            messagebox.showwarning("警告", "无法获取更新信息，请确保您已连接至支持IPv6的互联网")
        else:
            with urllib.request.urlopen(url) as response:
                update_ver = response.read().decode('utf-8').strip()
            ver = "1.19.511"
            if ver == update_ver:
                messagebox.showinfo("提示", "您使用的 ver "+ ver +" 版本为最新版本，无需更新")
                webbrowser.open("http://cmccprivatecloud.dynv6.net:9001/software/download.html")
            else:
                webbrowser.open("http://cmccprivatecloud.dynv6.net:9001/update.zip")

    def versioneggs():
        eggs.game()

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
        # messagebox.showinfo("提示",
        #                     f"多路识别目前仅支持录像识别\n视频源路径为：{localPath}\n识别默认为四路720P视频流\n合成结束后自动开始识别")
        print(f"传递的视频文件夹路径为：{localPath}")
        Video_Post.combiner(localPath)
        localPath = localPath + "\\output.mp4"
        print(localPath)

        GPUDevices = 0
        try:
            result = subprocess.run(['nvidia-smi', '--list-gpus'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if "NVIDIA" in result.stdout.decode():
                GPUDevices = 1
        except:
            pass

        if GPUDevices == 1:
            advancedDetector.advancedPro(localPath, 6)
        else:
            detectorlite.detector(XMLPath, localPath, TensorPath, a)

        # 显示窗口
        root.deiconify()
        print("多路监控：视频源：", localPath, "，数据集模型输入源：", XMLPath)

    # 帮助菜单
    def cloudtraining():
        messagebox.showinfo("帮助",f"单路监控:\n  1.基础识别:使用CPU进行目标识别，默认识别对象为人脸/行人身体/行人\n  "
                                   f"2.高级识别:使用GPU进行目标识别，默认加载已训练好的模型，使用PyTorch/YOLOv5进行目标识别，"
                                   f"支持更高的精确度和目标种类\n\n多路监控:\n  "
                                   f"1.合成并识别:合成四路视频，自动判断CPU/GPU识别方法，调用基础/高级识别(仅支持NVIDIA GPU)"
                                   f"\n\n模型训练:\n  1.本地训练:默认使用CPU进行训练\n  2.连接到服务器:使用GPU进行训练\n\n"
                                   f"北方工业大学 计19-3 钱晟"
                                   f"\n指导老师: 朱孟笑\n\n"
                                   f"Copyright © 2023 Sheng Qian.\n All rights reserved.\n")

    #机器学习模块
    def tensor():
        global TensorPath, a
        a = 2
        TensorPath = ml_entry.get()
        p = 1
        root.withdraw()
        if TensorPath:
            tfm.processBar(TensorPath)
            root.deiconify()
        else:
            messagebox.showwarning("警告", f"文件路径不能为空")
            root.deiconify()
        print("机器学习：机器学习文件源：", TensorPath)

    #高级识别功能
    def yolo_advanced():
        root.withdraw()
        global localPath, TensorPath, XMLPath, a
        localPath = video_entry.get()
        XMLPath = dataset_entry.get()
        TensorPath = ml_entry.get()
        if not localPath:
            a = 5
        else:
            a = 6
        advancedDetector.advancedPro(localPath, a)
        root.deiconify()

    def connecttoserver():
        root.destroy()
        server.GPUConnect()

    def bw():
        root.withdraw()
        global localPath
        localPath = video_entry.get()
        output_path = blackwhite.pluginbw(localPath)
        print(output_path)
        advancedDetector.advancedPro(output_path, 6)
        root.deiconify()


    # 绑定按钮响应函数
    single_btn.config(command=local)
    multi_btn.config(command=combine)
    ml_btn.config(command=tensor)
    ml_advanced.config(command=yolo_advanced)
    ml_exitprogram.config(command=cloudtraining)
    ml_server.config(command=connecttoserver)
    eggsv.config(command=versioneggs)
    update.config(command=upper)
    blackwhiteb.config(command=bw)

    # 运行主循环
    root.mainloop()



if __name__ == '__main__':
    main()
