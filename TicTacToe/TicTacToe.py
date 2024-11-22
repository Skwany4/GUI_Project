import customtkinter
import tkinter
from tkinter import messagebox
import random


class TicTacToe(customtkinter.CTkFrame):
    def __init__(self, app, vsAI=False):
        super().__init__(app.tk)
        self.board = ['-' for _ in range(9)]
        self.app = app
        self.symbol = 'X'
        self.vsAI = vsAI

        self.configure(fg_color="#0D1321")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        game_frame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=700)
        game_frame.grid_propagate(False)

        game_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        game_frame.grid_columnconfigure(0, weight=1)

        TopLabel = customtkinter.CTkLabel(game_frame, text="Tic Tac Toe", fg_color="#1D2D44", text_color="#FFFFFF",font=("Roboto", 40, "bold"), height=150)
        TopLabel.grid(row=0, column=0, pady=20)

        self.status_label = customtkinter.CTkLabel(game_frame, text=f"{self.symbol}'s turn", font=("Roboto", 20),
                                                  text_color="white")
        self.status_label.grid(row=1, column=0, pady=10)

        self.boardFrame = customtkinter.CTkFrame(game_frame, fg_color="#343A40")
        self.boardFrame.grid(row=2, column=0, pady=10)

        self.buttons = []
        for i in range(9):
            button = customtkinter.CTkButton(self.boardFrame, text="", width=100, height=100, font=("Roboto", 20), command=lambda idx=i: self.playerMove(idx), fg_color="#748CAB")
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        reset_button = customtkinter.CTkButton(game_frame, text="Reset Game", fg_color="#3E5C76", text_color="#FFFFFF",
                                                height=50, width=300, corner_radius=25, font=("Roboto", 20, "bold"),
                                                command=self.resetGame)
        reset_button.grid(row=6, column=0, pady=20)

        game_frame.grid(row=0, column=0, padx=20, pady=20)

    def playerMove(self, position):
        if self.board[position] == "-":
            self.board[position] = self.symbol
            self.updateButtons()
            if not self.checkResult():
                self.symbol = "O" if self.symbol == "X" else "X"
                self.status_label.configure(text=f"{self.symbol}'s turn")
                if self.vsAI and self.symbol == "O":
                    self.disableButtons()
                    self.after(500, self.delayedAiMove)

    def delayedAiMove(self):
        self.aiMove()

    def aiMove(self):
        available_positions = [i for i, spot in enumerate(self.board) if spot == '-']
        if available_positions:
            position = random.choice(available_positions)
            self.board[position] = self.symbol
            self.updateButtons()
            if not self.checkResult():
                self.symbol = "X"
                self.status_label.configure(text=f"{self.symbol}'s turn")
                self.enableButtons()
    def updateButtons(self):
        for i, btn in enumerate(self.buttons):
            btn.configure(text=self.board[i] if self.board[i] != "-" else "")

    def checkResult(self):
        if ((self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X') or
            (self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X') or
            (self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X') or
            (self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X') or
            (self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X') or
            (self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X') or
            (self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X') or
            (self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X')):
            self.status_label.configure(text=f"{self.symbol} wins!")
            if self.symbol == 'X' and self.vsAI:
                self.app.updateUserScore(10)
            self.disableButtons()
            self.endGameNoti()
            return True
        elif ((self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O') or
              (self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O') or
              (self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O') or
              (self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O') or
              (self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O') or
              (self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O') or
              (self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O') or
              (self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O')):
            self.status_label.configure(text=f"{self.symbol} wins!")
            self.disableButtons()
            self.endGameNoti()
            return True
        elif (self.board[0] != '-' and self.board[1] != '-' and self.board[2] != '-' and
              self.board[3] != '-' and self.board[4] != '-' and self.board[5] != '-' and
              self.board[6] != '-' and self.board[7] != '-' and self.board[8] != '-'):
            self.status_label.configure(text="Draw!")
            self.disableButtons()
            self.endGameNoti()
            return True
        return False

    def disableButtons(self):
        for btn in self.buttons:
            btn.configure(state="disabled")

    def enableButtons(self):
        for i, btn in enumerate(self.buttons):
            if self.board[i] == "-":
                btn.configure(state="normal")

    def resetGame(self):
        self.board = ['-' for _ in range(9)]
        self.symbol = 'X'
        self.status_label.configure(text=f"{self.symbol}'s turn")
        for btn in self.buttons:
            btn.configure(text="", state="normal")

    def endGameNoti(self):
        result = messagebox.askyesno("Games Platform", "Your game is over! Do you want to play again?")
        if result:
            self.resetGame()
        else:
            self.app.showSelectGame()
