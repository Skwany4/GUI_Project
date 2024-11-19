import tkinter
import customtkinter

from Connect4 import Connect4
from MainMenu import MainMenu
from LoginPanel import LoginPanel
from RegisterPanel import RegisterPanel
from RockScissorsPaper import RockScissorsPaper
from SelectGame import SelectGame
from TicTacToe import TicTacToe
#from SlideGame import SlideGame

customtkinter.set_appearance_mode("light")

class mainApp:
    def __init__(self,tk):
        self.tk = tk
        self.tk.title("Games Platform")
        self.tk.geometry("1280x720")
        self.tk.resizable(False, False)

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

    def showRockScissorsPaper(self):
        Rock_Scissors_Paper = RockScissorsPaper(self)
        self.showWindow(Rock_Scissors_Paper)

    # def showSlideGame(self):
    #     Slide_Game = SlideGame(self)
    #     self.showWindow(Slide_Game)


if __name__ == "__main__":
    ctk = customtkinter.CTk()
    app = mainApp(ctk)
    ctk.mainloop()