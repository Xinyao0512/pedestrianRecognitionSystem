# © Copyright 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
出错处理
"""

import os
import filetype
from tkinter import messagebox

#多路监控出错处理
def mp4_count(folder_path):

    #空文件夹检测
    if not folder_path:
        messagebox.showwarning("警告", "文件路径不能为空")
        return 1

    #视频流检查
    mp4_count = 0

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):

        # 遍历当前文件夹中的所有文件
        for file in files:

            # 检查文件扩展名是否为mp4
            if file.endswith('.mp4'):
                mp4_count += 1

    #视频流数量检测
    if mp4_count < 4 :
        messagebox.showwarning("警告", "文件夹中视频少于四条")
        return 1

#单路监控出错处理
def video_check(mp4_path):
    kind = filetype.guess(mp4_path)
    if kind is None:
        print('Cannot guess file type!')
        return 1
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
