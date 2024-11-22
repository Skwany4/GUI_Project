import customtkinter
import tkinter
from PIL import Image, ImageTk

class Connect4Select(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createConnect4Select()
        self.configure(fg_color="#0D1321")

    def createConnect4Select(self):
        TopLabelFrame = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#1D2D44", text_color="#FFFFFF",
                                               font=("Roboto", 40, "bold"), height=100)

        logoImage = customtkinter.CTkImage(Image.open("Menu/Images/Logo.png"), size=(400, 100))
        logoLabel = customtkinter.CTkLabel(TopLabelFrame, text="", image=logoImage)

        TopLabelFrame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        logoLabel.grid(row=0, column=0, columnspan=2, sticky="nsew")

        vsComputerButton = customtkinter.CTkButton(self, text="vs Player", fg_color="#3E5C76", text_color="#FFFFFF",
                                                   corner_radius=25, font=("Roboto", 20, "bold"), height=100, width=400,
                                                   command=self.app.showConnect4)
        vsComputerButton.grid(row=1, column=0, pady=(10, 20), padx=20)

        vsAIButton = customtkinter.CTkButton(self, text="vs Computer", fg_color="#3E5C76", text_color="#FFFFFF",
                                             corner_radius=25, font=("Roboto", 20, "bold"), height=100, width=400,
                                             command=self.app.showConnect4AI)
        vsAIButton.grid(row=2, column=0, pady=(10, 20), padx=20)

        self.BackArrowImage = customtkinter.CTkImage(Image.open("Menu/Images/BackArrow.png"), size=(50, 50))
        BackButton = customtkinter.CTkButton(self, image=self.BackArrowImage, text="", fg_color="transparent", hover=False, command=self.app.showSelectGame)
        BackButton.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
