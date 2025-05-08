# © Copyright 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

"""
此程序为CPU密集型程序
此程序为性能基准测试
在debug中使用
"""

import psutil
import tkinter as tk
import time

def performance_test():

    class CPUMonitor(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.usage_label = tk.Label(self, text='CPU Usage: ')
            self.usage_label.pack(side='left')
            self.usage_var = tk.StringVar()
            self.usage_var.set('0.0%')
            self.usage_value_label = tk.Label(self, textvariable=self.usage_var)
            self.usage_value_label.pack(side='left', padx=5)

            self.flops_label = tk.Label(self, text='CPU FLOPS: ')
            self.flops_label.pack(side='left')
            self.flops_var = tk.StringVar()
            self.flops_var.set('0 GFLOPS')
            self.flops_value_label = tk.Label(self, textvariable=self.flops_var)
            self.flops_value_label.pack(side='left', padx=5)

        def update(self):
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=0.5)
            self.usage_var.set(f'{cpu_percent:.1f}%')

            # Test CPU FLOPS
            start_time = time.time()
            for i in range(100000):
                a = 1.23456789
                b = 2.34567890
                c = a * b
            elapsed_time = time.time() - start_time
            flops = 100000 / elapsed_time / 1e9
            self.flops_var.set(f'{flops:.2f} GFLOPS')

            # Schedule next update
            self.after(1000, self.update)

    root = tk.Tk()
    root.title('CPU Monitor')
    monitor = CPUMonitor(root)
    monitor.update()
    monitor.mainloop()
