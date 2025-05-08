# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
机器学习模块
"""

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import numpy as np
import keras
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

import os
import time
import tkinter as tk
from tkinter import ttk, messagebox
import multiprocessing

print("tfm")

def processBar(folder_path):

  num_cores = multiprocessing.cpu_count()
  print(f"已检测到 {num_cores} 个 CPU 核心")
  messagebox.showinfo("提示",
                      f"已检测到 {num_cores} 个 CPU 核心")

  # 计算文件数量
  num_files = len([f for f in os.listdir(folder_path)
                   if os.path.isfile(os.path.join(folder_path, f))])

  # 创建Tkinter窗口
  root = tk.Tk()
  root.title("模型训练")
  root.geometry("300x120")
  root.iconbitmap("./img/intel.ico")
  root.resizable(False, False)

  # 创建标签和进度条
  label = tk.Label(root, text="正在使用CPU进行模型训练...", font=("Arial", 12))
  label.pack(pady=10)
  progress = ttk.Progressbar(root, orient=tk.HORIZONTAL,
                             length=200, mode='determinate')
  progress.pack(pady=10)

  # 创建百分比标签
  percent_label = tk.Label(root, text="0%", font=("Arial", 12))
  percent_label.pack()

  # 更新进度条和百分比
  for i in range(num_files):
    percent = int((i + 1) / num_files * 100)
    progress['value'] = percent
    percent_label.config(text=f"{percent}%")
    root.update()
    time.sleep(1)

  # 显示完成消息
  label.config(text="训练完成！", font=("Arial", 12))
  root.after(5000, root.destroy)
  machineLearning(folder_path , folder_path , 100)
  root.mainloop()


def machineLearning(dataset_path , model_dir , epochs):

  # 设置参数
  # dataset_path = 'D:/model'
  img_size = (224, 224)
  batch_size = 64
  # epochs = 1

  # 读取数据集
  X = []
  y = []
  for root, dirs, files in os.walk(dataset_path):
    for file in files:
      if file.endswith('.png'):
        img = load_img(os.path.join(root, file), target_size=img_size)
        img_arr = img_to_array(img)
        img_arr = preprocess_input(img_arr)
        X.append(img_arr)
        if 'positive' in file.lower():
          y.append(1)
        else:
          y.append(0)
  X = np.array(X)
  y = np.array(y)

  # 划分训练集和测试集
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # 构建模型
  base_model = VGG16(include_top=False, input_shape=img_size + (3,))
  model = Sequential()
  model.add(base_model)
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(1, activation='sigmoid'))

  # 编译模型
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

  # 数据增强
  train_datagen = ImageDataGenerator(rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                     horizontal_flip=True)
  train_generator = train_datagen.flow(X_train, y_train, batch_size=batch_size)

  # 训练模型
  model.fit(train_generator, steps_per_epoch=len(X_train) // batch_size, epochs=epochs)

  # 测试模型
  test_loss, test_acc = model.evaluate(X_test, y_test)
  print('Test accuracy:', test_acc)

  # 保存模型
  model.save(os.path.join(dataset_path, 'model.h5'))


