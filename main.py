import tkinter
import customtkinter
import sqlite3

from Menu import *
from Connect4 import *
from Menu.Profile import Profile
from TicTacToe import *
from Memory import Memory
from RockScissorsPaper import RockScissorsPaper
from Leaderboard import Leaderboard

customtkinter.set_appearance_mode("light")

class mainApp:
    def __init__(self,tk):
        self.tk = tk
        self.tk.title("Games Platform")
        self.tk.geometry("1280x720")
        self.tk.resizable(False, False)
        self.loggedUserId = None

        self.currentWindow = None
        self.showMainMenu()

    def showWindow(self,window):
        if self.currentWindow:
            self.currentWindow.pack_forget()

        self.currentWindow = window
        self.currentWindow.pack(fill = tkinter.BOTH, expand = True)

    def showMainMenu(self):
        menu = MainMenu(self)
        self.showWindow(menu)

    def showLoginPanel(self):
        login_panel = LoginPanel(self)
        self.showWindow(login_panel)

    def showRegisterPanel(self):
        registerPanel = RegisterPanel(self)
        self.showWindow(registerPanel)

    def showSelectGame(self):
        selectGame = SelectGame(self)
        self.showWindow(selectGame)

    def showTicTacToe(self):
        tic_tac_toe = TicTacToe(self)
        self.showWindow(tic_tac_toe)

    def showConnect4(self):
        Connect_4 = Connect4(self)
        self.showWindow(Connect_4)

    def showConnect4AI(self):
        Connect_4_AI = Connect4(self, vsAI = True)
        self.showWindow(Connect_4_AI)

    def showRockScissorsPaper(self):
        Rock_Scissors_Paper = RockScissorsPaper(self)
        self.showWindow(Rock_Scissors_Paper)

    def showConnect4Select(self):
        Connect_4_Select = Connect4Select(self)
        self.showWindow(Connect_4_Select)

    def showMemory(self):
        memoryGame = Memory(self)
        self.showWindow(memoryGame)

    def showTicTacToeAI(self):
        tic_tac_toe_ai = TicTacToe(self, vsAI=True)
        self.showWindow(tic_tac_toe_ai)

    def showTicTacToeSelect(self):
        tic_tac_toe_select = TicTacToeSelect(self)
        self.showWindow(tic_tac_toe_select)

    def showProfile(self,userId):
        show_Profile = Profile(self, userId)
        self.showWindow(show_Profile)

    def showLeaderboard(self):
        leaderboard = Leaderboard(self)
        self.showWindow(leaderboard)

    def updateUserScore(self, points):
        if self.loggedUserId is not None:
            conn = sqlite3.connect("Menu/Users.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET score = score + ? WHERE id_user = ?", (points, self.loggedUserId))
            conn.commit()
            conn.close()

if __name__ == "__main__":
    ctk = customtkinter.CTk()
    app = mainApp(ctk)
    ctk.mainloop()

# https://coolors.co/palette/0d1321-1d2d44-3e5c76-748cab-f0ebd8 #