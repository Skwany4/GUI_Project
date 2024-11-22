import numpy as np
import tkinter
import customtkinter
import random
from tkinter import messagebox


class Connect4(customtkinter.CTkFrame):
    def __init__(self, app, vsAI=False):
        super().__init__(app.tk)
        self.app = app
        self.board = createBoard()
        self.symbol = "🔴"
        self.vsAI = vsAI

        self.configure(fg_color="#0D1321")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        game_frame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=700, height=700)
        game_frame.grid_propagate(False)
        game_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        game_frame.grid_columnconfigure(0, weight=1)
        game_frame.grid(row=0, column=0, padx=20, pady=20)

        top_label = customtkinter.CTkLabel(game_frame, text="Connect 4", fg_color="#1D2D44", text_color="#FFFFFF",
                                           font=("Roboto", 40, "bold"), height=150)
        top_label.grid(row=0, column=0, pady=20)

        self.status_label = customtkinter.CTkLabel(game_frame, text=f"Player {self.symbol}'s turn", font=("Roboto", 20),
                                                   text_color="white")
        self.status_label.grid(row=1, column=0, pady=10)

        self.boardFrame = customtkinter.CTkFrame(game_frame, fg_color="#343A40")
        self.boardFrame.grid(row=2, column=0, pady=10)

        self.boardFrame.grid_rowconfigure(tuple(range(6)), weight=1)
        self.boardFrame.grid_columnconfigure(tuple(range(7)), weight=1)

        self.buttons = []
        for row in range(6):
            row_buttons = []
            for col in range(7):
                button = customtkinter.CTkButton(self.boardFrame, text="", width=80, height=80,
                                                 font=("Roboto", 20), fg_color="#748CAB",
                                                 command=lambda c=col: self.playerMove(c), corner_radius=40)
                button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        game_frame.grid(row=0, column=0, padx=20, pady=20)

    def playerMove(self, col):
        if checkMove(self.board, col):
            row = move(self.board, col, self.symbol)
            if row is not None:
                self.updateButtons()
                if checkWin(self.board, row, col, self.symbol):
                    self.status_label.configure(text=f"Player {self.symbol} wins!")
                    if self.symbol == "🔴" and self.vsAI:
                        self.app.updateUserScore(15)
                    self.disableButtons()
                    self.endGameNoti()
                else:
                    self.symbol = "🟡" if self.symbol == "🔴" else "🔴"
                    self.status_label.configure(text=f"Player {self.symbol}'s turn")
                if "-" not in self.board:
                    self.status_label.configure(text="Draw!")
                    self.disableButtons()
                    self.endGameNoti()
                elif self.vsAI and self.symbol == "🟡":
                    self.disableButtons()
                    self.after(500, self.aiMove)

    def aiMove(self):
        col = self.chooseAiMove()
        if col is not None:
            row = move(self.board, col, self.symbol)
            if row is not None:
                self.updateButtons()
                if checkWin(self.board, row, col, self.symbol):
                    self.status_label.configure(text=f"Player {self.symbol} wins!")
                    self.disableButtons()
                    self.endGameNoti()
                else:
                    self.symbol = "🔴"
                    self.status_label.configure(text=f"Player {self.symbol}'s turn")
                    self.enableButtons()

    def chooseAiMove(self):
        available_columns = [col for col in range(7) if checkMove(self.board, col)]
        if available_columns:
            return random.choice(available_columns)
        return None

    def updateButtons(self):
        for row in range(6):
            for col in range(7):
                symbol = self.board[row][col]
                color = "#FFFFFF"
                if symbol == "🔴":
                    color = "#FF0000"
                elif symbol == "🟡":
                    color = "#FFFF00"
                if symbol != "-":
                    self.buttons[row][col].configure(fg_color=color, text="")

    def disableButtons(self):
        for row in range(6):
            for col in range(7):
                self.buttons[row][col].configure(state="disabled")

    def enableButtons(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == "-":
                    self.buttons[row][col].configure(state="normal")

    def endGameNoti(self):
        result = messagebox.showinfo("Games Platform", "Your game is over!")
        if result == "ok":
            self.app.showSelectGame()

def createBoard():
    return np.full((6, 7), "-")


def checkMove(board, col):
    return 0 <= col < 7 and board[0][col] == "-"


def move(board, col, symbol):
    if checkMove(board, col):
        for row in range(len(board) - 1, -1, -1):
            if board[row][col] == "-":
                board[row][col] = symbol
                return row
    return None


def checkWin(board, row, col, symbol):
    return (checkDirection(board, row, col, symbol, 1, 0) or
            checkDirection(board, row, col, symbol, 0, 1) or
            checkDirection(board, row, col, symbol, 1, 1) or
            checkDirection(board, row, col, symbol, 1, -1))


def checkDirection(board, row, col, symbol, delta_row, delta_col):
    count = 0
    for i in range(-3, 4):
        r = row + i * delta_row
        c = col + i * delta_col
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False
