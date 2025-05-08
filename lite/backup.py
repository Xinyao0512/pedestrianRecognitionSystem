"""
登陆操作功能
"""

import hashlib
import tkinter as tk
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
        if username == "Admin" and password == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" :
            verification = 2
            root.destroy()
        if username != "Admin" or password != "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":
            messagebox.showwarning("警告","用户名或密码错误，程序即将退出")
            verification = 0
            root.destroy()

    def forgot_password():
        global ca
        global verification
        global ca
        ca = 0
        print("加密狗")
        with open('e:\\verification.pwd', 'r') as f:
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
    root.title("请登录")
    root.iconbitmap("./img/ncut.ico")
    root.geometry("300x210")

    # 标题
    root.input_1 = tk.Label(root, text="\n基于机器学习的行人识别系统", font=(10))
    root.input_1.pack(padx=5,pady=5)

    # 用户名输入
    username_label = tk.Label(root, text="用户名")
    username_label.pack(padx=50)
    username_entry = tk.Entry(root)
    username_entry.pack(padx=50)

    # 密码输入
    password_label = tk.Label(root, text="密码")
    password_label.pack(padx=50)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(padx=50)

    # 按钮
    button_frame = tk.Frame(root)
    button_frame.pack()

    login_button = tk.Button(button_frame, text="登录", command=login)
    login_button.pack(side="left", padx=5, pady=5)

    forgot_password_button = tk.Button(button_frame, text="加密狗", command=forgot_password)
    forgot_password_button.pack(side="left", padx=5, pady=5)

    #版本信息
    text_label = tk.Label(root, text="Beta 0.6.1")
    text_label.pack(side="right", padx=5)

    root.mainloop()

    return verification



def sql_check(username,password,ca):
    return 0

