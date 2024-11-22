import tkinter
import customtkinter
from PIL import Image


class SelectGame(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.configure(fg_color="#0D1321")  # Tło panelu
        self.createSelectGame()

    def createSelectGame(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ContentFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=700)
        ContentFrame.grid_propagate(False)

        ContentFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        ContentFrame.grid_columnconfigure(0, weight=1)

        TopLabel = customtkinter.CTkLabel(ContentFrame, text="Games Platform",font=("Roboto", 40, "bold"),text_color="#FFFFFF")

        TicTacToeButton = customtkinter.CTkButton(ContentFrame, text="Tic Tac Toe", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=self.app.showTicTacToeSelect)
        Connect4Button = customtkinter.CTkButton(ContentFrame, text="Connect 4", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=self.app.showConnect4Select)
        RockScissorsPaperButton = customtkinter.CTkButton(ContentFrame, text="Rock Scissors Paper", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=self.app.showRockScissorsPaper)
        SlideGameButton = customtkinter.CTkButton(ContentFrame, text="Memory game", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=self.app.showMemory)
        ProfileButton = customtkinter.CTkButton(ContentFrame, text="Profile", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=lambda: self.app.showProfile(self.app.loggedUserId))
        LeaderboardButton = customtkinter.CTkButton(ContentFrame, text="Leaderboard", fg_color="#3E5C76", text_color="#FFFFFF",height=80, width=400, corner_radius=25, font=("Roboto", 20, "bold"),command=self.app.showLeaderboard)

        TopLabel.grid(row=0, column=0, pady=20)
        TicTacToeButton.grid(row=1, column=0, pady=10)
        Connect4Button.grid(row=2, column=0, pady=10)
        RockScissorsPaperButton.grid(row=3, column=0, pady=10)
        SlideGameButton.grid(row=4, column=0, pady=10)
        ProfileButton.grid(row=5, column=0, pady=10)
        LeaderboardButton.grid(row=6, column=0, pady=10)

        ContentFrame.grid(row=0, column=0, padx=20, pady=20)
