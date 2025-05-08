import tkinter as tk
import time
from tkinter import messagebox
import datetime


def time_date():
    class App(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.time_label = tk.Label(self, font=('Arial', 20))
            self.time_label.pack(side="top", pady=10)
            self.update_clock()

        def update_clock(self):
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            self.time_label.configure(text=current_time)
            self.after(1, self.update_clock)

    root = tk.Tk()
    root.title("北方工业大学")
    root.resizable(False, False)
    root.iconbitmap("./img/ncut.ico")
    app = App(master=root)
    app.mainloop()
