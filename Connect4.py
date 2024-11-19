import numpy as np
import tkinter
import customtkinter

class Connect4(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.board = createBoard()
        self.symbol = "🔴"

        TopLabel = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#343A40",text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=150)
        self.status_label = customtkinter.CTkLabel(self, text=f"Player {self.symbol}'s turn",font=("Roboto", 20), text_color="black")
        self.boardFrame = customtkinter.CTkFrame(self, fg_color="#343A40")

        TopLabel.pack(fill=tkinter.X)
        self.status_label.pack(pady=10)
        self.boardFrame.pack()

        self.buttons = []
        for row in range(6):
            row_buttons = []
            for col in range(7):
                button = customtkinter.CTkButton(self.boardFrame, text="", width=80, height=80,font=("Roboto", 20),command=lambda c=col: self.playerMove(c))
                button.grid(row=row, column=col, padx=3, pady=3)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def playerMove(self, col):
        if checkMove(self.board, col):
            row = move(self.board, col, self.symbol)
            if row is not None:
                self.updateButtons()
                if checkWin(self.board, row, col, self.symbol):
                    self.status_label.configure(text=f"Player {self.symbol} wins!")
                    self.disableButtons()
                else:
                    self.symbol = "🟡" if self.symbol == "🔴" else "🔴"
                    self.status_label.configure(text=f"Player {self.symbol}'s turn")
                if "-" not in self.board:
                    self.status_label.configure(text="Draw!")
                    self.disableButtons()

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
                    self.buttons[row][col].configure(text=symbol,fg_color=color,text_color="black",state="normal" if symbol == "-" else "disabled")

    def disableButtons(self):
        for row in range(6):
            for col in range(7):
                self.buttons[row][col].configure(state="disabled")


def createBoard():
    return np.full((6,7),"-")

def checkMove(board,col):
    if 6 >= col >= 0  and board[0][col] == "-":
        return True
    else:
        return False

def move(board,col,symbol):
    if checkMove(board,col):
        for row in range(len(board)-1,-1,-1):
            if board[row][col] == '-':
                board[row][col] = symbol
                return row
    return None

def checkWin(board, row, col, symbol):
    return (checkDirection(board, row, col, symbol, 1, 0) or  # Poziomo
            checkDirection(board, row, col, symbol, 0, 1) or  # Pionowo
            checkDirection(board, row, col, symbol, 1, 1) or  # Ukośnie w dół
            checkDirection(board, row, col, symbol, 1, -1))   # Ukośnie w górę

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