# """
# 服务器连接
# """
#
# import tkinter as tk
# import subprocess
#
#
# def connect_test(server_address):
#
#     #连通性测试
#     def ping(host):
#         # 运行ping命令
#         result = subprocess.run(['ping', '-c', '1', '-W', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#         # 根据返回结果判断是否成功
#         if result.returncode == 0:
#             # 成功
#             return 1
#         else:
#             #失败
#             return 0
#
#     # 测试
#     host = server_address
#     if ping(host):
#         print("ping成功")
#     else:
#         print("ping失败")
#
# def connect_server(TensorPath):
#     # 创建窗口
#     window = tk.Tk()
#     window.title("服务器连接")
#     window.geometry("300x150")
#     window.iconbitmap("./img/connect.ico")
#
#     # 服务器地址输入框
#     address_label = tk.Label(window, text="服务器地址：")
#     address_label.pack()
#     address_entry = tk.Entry(window)
#     address_entry.pack()
#
#     # 端口输入框
#     port_label = tk.Label(window, text="端口号：")
#     port_label.pack()
#     port_entry = tk.Entry(window)
#     port_entry.pack()
#
#     null_label = tk.Label(window, text="")
#     null_label.pack()
#     # 创建按钮的Frame
#     button_frame = tk.Frame(window)
#     button_frame.pack()
#
#     # 连接到服务器按钮
#     def connect():
#         global s, server_address, server_port
#         server_address = address_entry.get()
#         server_port = port_entry.get()
#         s = 1
#         print(f"正在连接到服务器：{server_address}:{server_port}")
#         if connect_test(server_address) :
#             window.destroy()
#
#
#     connect_btn = tk.Button(button_frame, text="连接到服务器", command=connect)
#     connect_btn.pack(side=tk.LEFT, padx=5)
#
#     # 本地运行按钮
#     def run_locally():
#         global s
#         s = 0
#         if TensorPath:
#             print("已切换到本地运行模式")
#             window.destroy()
#
#     run_btn = tk.Button(button_frame, text="本地运行", command=run_locally)
#     run_btn.pack(side=tk.LEFT, padx=5)
#
#     return 1
#
#     # 主循环
#     s = -1
#     server_address = ""
#     server_port = ""
#     window.mainloop()
#

# © Copyright 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
登陆操作功能
"""

import tkinter as tk
from tkinter import *

#定义GPUTraining函数
def GPUTraining():
    #在此处添加GPUTraining的代码
    print("调用GPUTraining函数")

def GPUConnect():

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
    train_button = tk.Button(root, text="连接并训练", width=26, height=2, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    train_button.place(relx=0.155, rely=0.86, anchor=NW)

    #运行窗口
    root.mainloop()

GPUConnect()