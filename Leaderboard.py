import customtkinter
import sqlite3

class Leaderboard(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.configure(fg_color="#0D1321")
        self.createLeaderboard()

    def createLeaderboard(self):
        LeaderboardFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=600)
        LeaderboardFrame.grid_propagate(False)
        LeaderboardFrame.grid_columnconfigure(0, weight=1)
        LeaderboardFrame.grid_rowconfigure((0, 1, 2), weight=1)

        titleLabel = customtkinter.CTkLabel(LeaderboardFrame, text="Leaderboard", font=("Roboto", 30, "bold"),text_color="#FFFFFF")
        titleLabel.grid(row=0, column=0, pady=20)

        self.playersFrame = customtkinter.CTkFrame(LeaderboardFrame, fg_color="#1D2D44")
        self.playersFrame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        self.loadLeaderboard()

        backButton = customtkinter.CTkButton(LeaderboardFrame, text="Back", fg_color="#3E5C76", text_color="#FFFFFF",corner_radius=25, font=("Roboto", 20, "bold"), height=50,command=self.app.showSelectGame)
        backButton.grid(row=2, column=0, pady=20)

        LeaderboardFrame.grid(row=0, column=0, padx=20, pady=20)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def loadLeaderboard(self):
        conn = sqlite3.connect("Menu/Users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
        players = cursor.fetchall()
        conn.close()

        for widget in self.playersFrame.winfo_children():
            widget.destroy()

        for idx, (username, score) in enumerate(players, start=1):
            playerLabel = customtkinter.CTkLabel(self.playersFrame, text=f"{idx}. {username} - {score} pts",
                                                 font=("Roboto", 18), text_color="#FFFFFF", anchor="w")
            playerLabel.pack(fill="x", pady=5, padx=10)
