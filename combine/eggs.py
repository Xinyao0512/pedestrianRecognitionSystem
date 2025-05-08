# Copyright © 2023 Sheng Qian. All rights reserved.
# North China University of Technology, co.
# Computer Science 19-3
# 19101110207
# xinyaoqian694@gamil.com

import tkinter as tk
from tkinter import messagebox
import datetime

def game():
    # 获取当前日期
    today = datetime.date.today()

    # 将月份和日期存储在相应的变量中
    month = today.month
    date = today.day

    # 彩蛋日期判定
    if month == 1 and date ==19:
        special = 1
    elif month == 5 and date == 11:
        special = 1
    else:
        special = 0

    class TicTacToe:
        def __init__(self, master):
            self.master = master
            master.title("北方工业大学")
            root.resizable(False, False)

            # 设置窗口图标
            root.iconbitmap("./img/ncut.ico")

            self.current_player = "X"
            self.board = [[" ", " ", " "] for _ in range(3)]

            self.buttons = [[tk.Button(master, text=" ", font=("Helvetica", 20), height=4, width=8, command=lambda row=row, col=col: self.make_move(row, col)) for col in range(3)] for row in range(3)]
            for row in range(3):
                for col in range(3):
                    self.buttons[row][col].grid(row=row, column=col)

        def make_move(self, row, col):
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player
                self.buttons[row][col]["text"] = self.current_player
                if self.check_win(row, col):
                    if special == 0:
                        messagebox.showinfo("提示", f"敦品励学 才德并懋\n{self.current_player} 获胜")
                    if special == 1:
                        messagebox.showinfo("qs&zpy", "世界が海に変わりますように、あなたと私が最初の光景に戻りますように")
                    self.master.destroy()
                    self.reset_board()
                elif self.check_tie():
                    if special == 0:
                        messagebox.showinfo("提示", f"敦品励学 才德并懋\n 平局")
                    if special == 1:
                        messagebox.showinfo("qs&zpy", "何年も一緒にいてくれてありがとう")
                    self.master.destroy()
                    self.reset_board()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

        def check_win(self, row, col):
            return (self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player or
                    self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player or
                    self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or
                    self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player)

        def check_tie(self):
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        return False
            return True

        def reset_board(self):
            self.current_player = "X"
            self.board = [[" ", " ", " "] for _ in range(3)]
            for row in range(3):
                for col in range(3):
                    self.buttons[row][col]["text"] = " "

    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
