# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
服务器连接
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import urllib.request
import requests
import main
import re
import webbrowser

print("server")

#定义GPUTraining函数
def GPUTraining(url, port):
    #在此处添加GPUTraining的代码
    print("调用GPUTraining函数")
    url = "http://"+url
    # port = 80
    # 构建完整的URL，包括端口号
    full_url = '{}:{}'.format(url, port)
    if url != "http://cmccprivatecloud.dynv6.net":
        webbrowser.open("http://cmccprivatecloud.dynv6.net:9001/error.html")
        print("连接失败，程序将自动退出")
        exit(0)
    # 发起HTTP请求并检查响应代码
    try:
        response = urllib.request.urlopen(full_url)
        if response.getcode() == 200:
            tst = 200
            print("已提交连接请求，待服务器响应后自动开始训练")
            url2 = url + ":" + port + "/training.html"
            print(url2)
            # 在默认浏览器中打开指定的网页
            webbrowser.open(url2)
            headers = {
                'cookie': '_training_fp=default; accessToken=5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
            }

            # 设置请求的参数
            data = {
                'type': "xml",
                'img': "img",
                'num': 1,
                'label': "person",
                't': None
            }
            # 发送 POST 请求
            response = requests.post(url, headers=headers, json=data)
            print (response)
            exit(0)
        else:
            webbrowser.open("http://cmccprivatecloud.dynv6.net:9001/403.html")
            print("连接失败，程序将自动退出")
    except Exception as e:
        webbrowser.open("http://cmccprivatecloud.dynv6.net:9001/error.html")
        print('连接失败：{}'.format(e))
        print("连接失败，程序将自动退出")


def GPUConnect():

    def set_ser():
        nonlocal ser
        ipaddr = ip_entry.get()  # 获取IP地址
        port = port_entry.get()
        ser = 1
        # if ipaddr == "cmccprivatecloud.dynv6.net" and port:
        if ipaddr and port:
            root.destroy()
            print(ser)
            print(ipaddr, port)
            GPUTraining(ipaddr, port)

    #创建窗口
    root = tk.Tk()
    root.geometry("320x480") #窗口大小为320*480
    root.title("连接到GPU服务器")
    root.resizable(False, False)

    # 设置窗口图标
    root.iconbitmap("./img/connect.ico")

    #设置背景图片
    bg_image = tk.PhotoImage(file="./img/GPUServer.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # 设置输入框样式
    entry_style = {"background": "#f0f5ff", "highlightthickness": 0, "border": 0}

    #创建IP输入框
    ip_entry = tk.Entry(root, width=35, **entry_style)
    ip_entry.place(relx=0.12, rely=0.615, anchor=NW)

    #创建端口输入框
    port_entry = tk.Entry(root, width=35, **entry_style)
    port_entry.place(relx=0.12, rely=0.75, anchor=NW)

    # 设置字体
    button_font = {"size": 20, "weight": "bold"}

    #创建连接并训练按键
    train_button = tk.Button(root, text="连接并训练", width=26, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font, command=lambda: set_ser())
    train_button.place(relx=0.155, rely=0.86, anchor=NW)

    #初始化ser值为0
    ser = 0

    #运行窗口
    root.mainloop()


# GPUConnect()