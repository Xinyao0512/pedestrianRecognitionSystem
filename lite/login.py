# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
登陆操作功能
"""

print("login")

import hashlib
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from logging import root
from tkinter import messagebox

import notification



def verification():
    try:
        with open('e:\\verification.pwd', 'r') as f:
            text = f.read()
            return text
            print(text)
    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print("读取文件时发生错误：", e)
    finally:
        f.close()


def sys_login():

    ca = -1  # 默认值为-1

    def login():
        global ca
        global verification

        ca = 1
        username = username_entry.get()
        password = hashlib.sha256(password_entry.get().encode()).hexdigest()
        print("用户名: {}".format(username))
        print("密码: {}".format(password))
        # 打印ca的值
        print("ca =", ca)
        with open('f:\\user.usr', 'r') as f:
            usr = f.read()
            print(usr)
        with open('f:\\password.pwd', 'r') as f:
            pwd = f.read()
            print(pwd)
        if username == usr and password == pwd :
            verification = 2
            root.destroy()
        if username != usr or password != pwd:
            messagebox.showwarning("警告","用户名或密码错误，程序即将退出")
            verification = 0
            root.destroy()

    def forgot_password():
        global ca
        global verification
        global ca
        ca = 0
        print("加密狗")
        with open('f:\\verification.pwd', 'r') as f:
            text = f.read()
            print(text)
        if text == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" :
            verification = 2
            root.destroy()
        else :
            exit (0)

        # 打印ca的值
        print("ca =", ca)

    root = tk.Tk()
    root.geometry('384x512')
    root.title('北方工业大学')
    root.iconbitmap("./img/ncut.ico")
    root.resizable(False, False)

    # 设置窗口背景
    bg_image = tk.PhotoImage(file='./img/login_mini.png')
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_style = {"background": "#f0f5ff", "highlightthickness": 0, "border": 0}

    username_entry = tk.Entry(root, width=39, **entry_style)
    username_entry.place(relx=0.15, rely=0.64, anchor=NW)

    password_entry = tk.Entry(root, show="*", width=39, **entry_style)
    password_entry.place(relx=0.15, rely=0.77, anchor=NW)

    # 按钮
    button_font = {"size": 20, "weight": "bold"}
    login_button = tk.Button(root, text="登录", command=login,width=13, height=1, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    login_button.place(relx=0.16, rely=0.875, anchor=NW)

    forgot_password_button = tk.Button(root, text="加密狗", command=forgot_password,width=13, height=1, highlightthickness=0, bd=0, bg="#3777f6", fg="white", activebackground="#3777f6", font=button_font)
    forgot_password_button.place(relx=0.55, rely=0.875, anchor=NW)

    #版本信息
    text_label = tk.Label(root, text="ver 1.19.511_CPU", background="white")
    text_label.place(relx=0.72, rely=0.95, anchor=NW)

    root.mainloop()

    return verification



def sql_check(username,password,ca):
    return 0

