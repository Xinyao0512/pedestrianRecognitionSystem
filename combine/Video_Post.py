# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
图像处理模块，实现多路图像合并
保存为两个文件
合并后的原分辨率文件为output.mp4
文件保存到原视频所在的文件夹中
"""

from moviepy.editor import *
import os
import notification

print("Video_Post")

def combiner(video_folder):
    # 定义视频文件夹路径
    # video_folder = "D:\\System folder\\Desktop\\1"

    # 获取文件夹中的所有视频文件
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

    # 按照文件名排序
    video_files = sorted(video_files)

    # 创建一个数组来保存每个视频文件的VideoFileClip对象
    clips = []

    # 为每个视频文件创建VideoFileClip对象
    for filename in video_files:
        filepath = os.path.join(video_folder, filename)
        clip = VideoFileClip(filepath)
        clips.append(clip)

    # 将四个视频文件合成为一个4路视频
    final_clip = clips_array([[clips[0], clips[1]], [clips[2], clips[3]]])

    # 调整视频分辨率为720p
    final_clip = final_clip.resize(height=720)

    # 定义输出文件路径
    output_file = os.path.join(video_folder, "output.mp4")

    # 输出合成的视频文件
    final_clip.write_videofile(output_file, fps=30)
    output_path = video_folder + "\\output.mp4"
    #显示完成信息
    notification.notice_video_complete()
    return output_path
