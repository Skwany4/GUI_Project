import customtkinter
import tkinter


class TicTacToe(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.board = ['-' for _ in range(9)]
        self.app = app
        self.symbol = 'X'
        TopLabel = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#343A40", text_color="#FFFFFF",
                                          font=("Roboto", 40, "bold"), height=150)
        TopLabel.pack(fill=tkinter.X)
        self.status_label = customtkinter.CTkLabel(self, text=f"Player {self.symbol}'s turn", font=("Roboto", 20), text_color="black")
        self.status_label.pack(pady=10)

        self.boardFrame = customtkinter.CTkFrame(self, fg_color="#343A40")
        self.boardFrame.pack()

        self.buttons = []
        for i in range(9):
            button = customtkinter.CTkButton(self.boardFrame, text="", width=100, height=100, font=("Roboto", 20), command=lambda idx=i: self.playerMove(idx))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)


    def playerMove(self, position):
        if self.board[position] == "-":
            self.board[position] = self.symbol
            self.updateButtons()
            if not self.checkResult():
                self.symbol = "O" if self.symbol == "X" else "X"
                self.status_label.configure(text=f"Player {self.symbol}'s turn")

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
            self.status_label.configure(text=f"Player {self.symbol} wins!")
            self.disableButtons()
            return True
        elif ((self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O') or
              (self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O') or
              (self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O') or
              (self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O') or
              (self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O') or
              (self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O') or
              (self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O') or
              (self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O')):
            self.status_label.configure(text=f"Player {self.symbol} wins!")
            self.disableButtons()
            return True
        elif (self.board[0] != '-' and self.board[1] != '-' and self.board[2] != '-' and
              self.board[3] != '-' and self.board[4] != '-' and self.board[5] != '-' and
              self.board[6] != '-' and self.board[7] != '-' and self.board[8] != '-'):
            self.status_label.configure(text="Draw!")
            self.disableButtons()
            return True
        return False

    def disableButtons(self):
        for btn in self.buttons:
            btn.configure(state="disabled")
