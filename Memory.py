import tkinter
import customtkinter
import random
from tkinter import messagebox


class Memory(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.boardSize = 4
        self.cards = ['🍎', '🍌', '🍇', '🍒', '🍉', '🍓', '🍑', '🍍'] * 2  # 8 pairs of emojis
        random.shuffle(self.cards)

        self.configure(fg_color="#0D1321")
        self.selectedCards = []
        self.matchedCards = []
        self.attempts = 0

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ContentFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=700)
        ContentFrame.grid_propagate(False)
        ContentFrame.grid_rowconfigure((0, 1, 2), weight=1)
        ContentFrame.grid_columnconfigure(0, weight=1)
        ContentFrame.grid(row=0, column=0, padx=20, pady=20)

        TopLabel = customtkinter.CTkLabel(ContentFrame, text="Memory Game",font=("Roboto", 40, "bold"), text_color="#FFFFFF")
        TopLabel.grid(row=0, column=0, pady=20)

        self.statusLabel = customtkinter.CTkLabel(ContentFrame, text=f"Attempts: {self.attempts}",font=("Roboto", 20), text_color="#FFFFFF")
        self.statusLabel.grid(row=1, column=0, pady=10)

        self.boardFrame = customtkinter.CTkFrame(ContentFrame, fg_color="transparent")
        self.boardFrame.grid(row=2, column=0, pady=20)

        self.buttons = []
        for i in range(self.boardSize * self.boardSize):
            button = customtkinter.CTkButton(self.boardFrame, text="", width=100, height=100, font=("Roboto", 20),fg_color="#3E5C76", text_color="#FFFFFF", corner_radius=25,command=lambda idx=i: self.playerMove(idx))
            button.grid(row=i // self.boardSize, column=i % self.boardSize, padx=5, pady=5)
            self.buttons.append(button)

    def playerMove(self, position):
        if position in self.matchedCards or position in self.selectedCards:
            return

        currentButton = self.buttons[position]
        currentButton.configure(text=self.cards[position])
        self.selectedCards.append(position)

        if len(self.selectedCards) == 2:
            self.attempts += 1
            self.statusLabel.configure(text=f"Attempts: {self.attempts}")

            firstPos, secondPos = self.selectedCards
            if self.cards[firstPos] == self.cards[secondPos]:
                self.matchedCards.extend(self.selectedCards)
                for pos in self.selectedCards:
                    self.buttons[pos].configure(state="disabled")
                self.selectedCards = []
            else:
                for button in self.buttons:
                    button.configure(state="disabled")
                self.after(500, self.hideCards)

            if len(self.matchedCards) == len(self.cards):
                self.endGame()

    def hideCards(self):
        for pos in self.selectedCards:
            self.buttons[pos].configure(text="")

        self.selectedCards = []

        for i, button in enumerate(self.buttons):
            if i not in self.matchedCards:
                button.configure(state="normal")

    def endGame(self):
        messagebox.showinfo("Memory Game", f"Congratulations! You won in {self.attempts} attempts!")
        self.app.updateUserScore(20)
        self.app.showSelectGame()
