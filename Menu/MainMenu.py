import tkinter
import customtkinter
from PIL import Image, ImageTk


class MainMenu(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createMainMenu()
        self.configure(fg_color="#0D1321")

    def createMainMenu(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        #TopLabel = customtkinter.CTkLabel(self,text="Games Platform", fg_color="#343A40", text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=150)
        LoginFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=600)
        LoginFrame.grid_propagate(False)
        LoginFrame.grid_columnconfigure(0, weight=1)
        LoginFrame.grid_rowconfigure((0,1), weight=1)
        logoImage = customtkinter.CTkImage(Image.open("Menu/Images/Logo.png"), size=(400,100))
        logoLabel = customtkinter.CTkLabel(LoginFrame, text="", image=logoImage)

        LoginButton = customtkinter.CTkButton(LoginFrame, text="Log in", fg_color="#3E5C76", text_color="#FFFFFF", font=("Roboto", 30), border_width=0, height=100, width=300,corner_radius=25,command=self.app.showLoginPanel)
        RegisterButton = customtkinter.CTkButton(LoginFrame, text="Register", fg_color="#3E5C76", text_color="#FFFFFF", font=("Roboto", 30), border_width=0, height=100, width=300,corner_radius=25,command=self.app.showRegisterPanel)


        #TopLabel.pack(fill=customtkinter.X)

       # LoginButton.pack(pady=50, padx=50)
       # RegisterButton.pack(pady=50, padx=50)
        LoginFrame.grid(row=0, column=0)
        logoLabel.grid(row=0, column=0, padx=50)
        LoginButton.grid(row = 1, column = 0, padx = 20, pady = 20)
        RegisterButton.grid(row = 2, column = 0, padx = 20, pady = 20)

