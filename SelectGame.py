import tkinter
import customtkinter

class SelectGame(tkinter.Frame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createSelectGame()

    def createSelectGame(self):

        TopLabel = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#343A40", text_color="#FFFFFF",
                                          font=("Roboto", 40, "bold"), height=150)

        TicTacToeButton = customtkinter.CTkButton(self, text="Tic Tac Toe", fg_color="#343A40", hover=False, height=100, width=400, corner_radius=20,font=("Roboto", 20, "bold"), command=self.app.showTicTacToe)
        Connect4Button = customtkinter.CTkButton(self, text="Connect 4", fg_color="#343A40", hover=False,height=100, width=400, corner_radius=20,font=("Roboto", 20, "bold"))
        RockScissorsPaperButton = customtkinter.CTkButton(self, text="Rock Scissors Paper", fg_color="#343A40", hover=False,height=100, width=400, corner_radius=20,font=("Roboto", 20, "bold"))
        Game4Button = customtkinter.CTkButton(self, text="Game 4", fg_color="#343A40", hover=False,height=100, width=400, corner_radius=20,font=("Roboto", 20, "bold"))

        TopLabel.pack(fill=tkinter.X)
        TicTacToeButton.pack(pady=10, padx=10)
        Connect4Button.pack(pady=10, padx=10)
        RockScissorsPaperButton.pack(pady=10, padx=10)
        Game4Button.pack(pady=10, padx=10,)