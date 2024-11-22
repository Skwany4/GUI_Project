import tkinter
import customtkinter
import random
from tkinter import messagebox


class RockScissorsPaper(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.board = ["Rock", "Scissors", "Paper"]
        self.playerScore = 0
        self.computerScore = 0
        self.configure(fg_color="#0D1321")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ContentFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=700)
        ContentFrame.grid_propagate(False)
        ContentFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        ContentFrame.grid_columnconfigure(0, weight=1)

        TopLabel = customtkinter.CTkLabel(ContentFrame, text="Rock Scissors Paper",font=("Roboto", 40, "bold"), text_color="#FFFFFF")
        TopLabel.grid(row=0, column=0, pady=20)

        self.scoreLabel = customtkinter.CTkLabel(ContentFrame, text=f"Score -> Player: {self.playerScore}, Computer: {self.computerScore}",font=("Roboto", 20), text_color="#FFFFFF")
        self.scoreLabel.grid(row=1, column=0, pady=10)
        self.statusLabel = customtkinter.CTkLabel(ContentFrame, text="Make your move!",font=("Roboto", 18), text_color="#FFFFFF")
        self.statusLabel.grid(row=2, column=0, pady=10)
        self.buttonsFrame = customtkinter.CTkFrame(ContentFrame, fg_color="transparent")
        self.buttonsFrame.grid(row=3, column=0, pady=20)
        self.rockButton = customtkinter.CTkButton(self.buttonsFrame, text="Rock", command=lambda: self.handlePlayerMove(0),font=("Roboto", 18), fg_color="#3E5C76", text_color="#FFFFFF", corner_radius=25, width=120, height=50)
        self.rockButton.grid(row=0, column=0, padx=10, pady=10)

        self.scissorsButton = customtkinter.CTkButton(self.buttonsFrame, text="Scissors", command=lambda: self.handlePlayerMove(1),font=("Roboto", 18), fg_color="#3E5C76", text_color="#FFFFFF", corner_radius=25,width=120, height=50)
        self.scissorsButton.grid(row=0, column=1, padx=10, pady=10)

        self.paperButton = customtkinter.CTkButton(self.buttonsFrame, text="Paper", command=lambda: self.handlePlayerMove(2),font=("Roboto", 18), fg_color="#3E5C76", text_color="#FFFFFF", corner_radius=25,width=120, height=50)
        self.paperButton.grid(row=0, column=2, padx=10, pady=10)

        self.resetButton = customtkinter.CTkButton(ContentFrame, text="Reset Game", command=self.resetGame,font=("Roboto", 16), fg_color="gray", text_color="white", corner_radius=25,width=150, height=40)
        self.resetButton.grid(row=4, column=0, pady=20)

        ContentFrame.grid(row=0, column=0, padx=20, pady=20)


    def handlePlayerMove(self, playerMove):
        self.disableButtons()
        self.statusLabel.configure(text=f"Player chose {self.board[playerMove]}...",text_color="#FFFFFF")
        self.after(1000, lambda: self.revealComputerMove(playerMove))

    def revealComputerMove(self, playerMove):
        computerMove = random.randint(0, 2)
        self.statusLabel.configure(text=f"Player chose {self.board[playerMove]}, Computer chose {self.board[computerMove]}.",text_color="#FFFFFF")
        self.after(1000, lambda: self.processRound(playerMove, computerMove))

    def processRound(self, playerMove, computerMove):
        result = self.results(playerMove, computerMove)
        self.playerScore += result[0]
        self.computerScore += result[1]
        self.scoreLabel.configure(text=f"Score -> Player: {self.playerScore}, Computer: {self.computerScore}")
        if self.checkWin():
            self.disableButtons()
        else:
            self.enableButtons()

    def results(self,playerMove, computerMove):
        if playerMove == computerMove:
            self.statusLabel.configure(text="It's a draw!", text_color="blue")
            return 0, 0
        elif (playerMove == 0 and computerMove == 1) or \
             (playerMove == 1 and computerMove == 2) or \
             (playerMove == 2 and computerMove == 0):
            self.statusLabel.configure(text="You win this round!", text_color="green")
            return 1, 0
        else:
            self.statusLabel.configure(text="Computer wins this round!", text_color="red")
            return 0, 1

    def checkWin(self):
        if self.playerScore == 3:
            self.statusLabel.configure(text="Congratulations! You won the game!", text_color="green")
            self.app.updateUserScore(5)
            self.endGameNoti()
            return True
        elif self.computerScore == 3:
            self.statusLabel.configure(text="Oh no! The computer won the game.", text_color="red")
            self.endGameNoti()
            return True
        return False

    def disableButtons(self):
        self.rockButton.configure(state="disabled")
        self.scissorsButton.configure(state="disabled")
        self.paperButton.configure(state="disabled")

    def enableButtons(self):
        self.rockButton.configure(state="normal")
        self.scissorsButton.configure(state="normal")
        self.paperButton.configure(state="normal")

    def resetGame(self):
        self.playerScore = 0
        self.computerScore = 0
        self.scoreLabel.configure(text=f"Score -> Player: {self.playerScore}, Computer: {self.computerScore}")
        self.statusLabel.configure(text="Make your move!", text_color="black")
        self.enableButtons()

    def endGameNoti(self):
        result = messagebox.showinfo("Games Platform", "Your game is over!")
        if result == "ok":
            self.app.showSelectGame()