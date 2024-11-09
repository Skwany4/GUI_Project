import tkinter
import customtkinter

from MainMenu import MainMenu
from LoginPanel import LoginPanel
from RegisterPanel import RegisterPanel
from SelectGame import SelectGame
from TicTacToe import TicTacToe

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


if __name__ == "__main__":
    ctk = customtkinter.CTk()
    app = mainApp(ctk)
    ctk.mainloop()