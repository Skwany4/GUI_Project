import tkinter
import customtkinter
import random

board = ["Rock", "Scissors", "Paper"]

class RockScissorsPaper(customtkinter.CTkFrame):
    def __init__(self,app):
        super().__init__(app.tk)
        self.app = app
        self.board = ["Rock", "Scissors", "Paper"]
        self.playerScore = 0
        self.computerScore = 0

        TopLabel = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#343A40",text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=100)
        self.scoreLabel = customtkinter.CTkLabel(self,text=f"Score -> Player: {self.playerScore}, Computer: {self.computerScore}",font=("Roboto", 20), text_color="black")
        self.statusLabel = customtkinter.CTkLabel(self,text="Make your move!",font=("Roboto", 18), text_color="black")
        self.buttonsFrame = customtkinter.CTkFrame(self, fg_color="transparent")

        self.rockButton = customtkinter.CTkButton(self.buttonsFrame, text="Rock",command=lambda: self.handlePlayerMove(0),font=("Roboto", 18), width=120, height=50)
        self.scissorsButton = customtkinter.CTkButton(self.buttonsFrame, text="Scissors",command=lambda: self.handlePlayerMove(1),font=("Roboto", 18), width=120, height=50)
        self.paperButton = customtkinter.CTkButton(self.buttonsFrame, text="Paper",command=lambda: self.handlePlayerMove(2),font=("Roboto", 18), width=120, height=50)

        self.resetButton = customtkinter.CTkButton(self, text="Reset Game", command=self.resetGame,font=("Roboto", 16), fg_color="gray", text_color="white",width=150, height=40)

        TopLabel.pack(fill=tkinter.X, pady=(0, 20))
        self.scoreLabel.pack(pady=10)
        self.statusLabel.pack(pady=10)
        self.buttonsFrame.pack(pady=20)

        self.rockButton.grid(row=0, column=0, padx=10, pady=10)
        self.scissorsButton.grid(row=0, column=1, padx=10, pady=10)
        self.paperButton.grid(row=0, column=2, padx=10, pady=10)

        self.resetButton.pack(pady=20)

    def handlePlayerMove(self, playerMove):
        self.disableButtons()
        self.statusLabel.configure(text=f"Player chose {self.board[playerMove]}...",text_color="black")
        self.after(1000, lambda: self.revealComputerMove(playerMove))

    def revealComputerMove(self, playerMove):
        computerMove = random.randint(0, 2)
        self.statusLabel.configure(text=f"Player chose {self.board[playerMove]}, Computer chose {self.board[computerMove]}.",text_color="black")
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
            return True
        elif self.computerScore == 3:
            self.statusLabel.configure(text="Oh no! The computer won the game.", text_color="red")
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