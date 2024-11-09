import tkinter
import customtkinter

class MainMenu(tkinter.Frame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createMainMenu()

    def createMainMenu(self):

        TopLabel = customtkinter.CTkLabel(self,text="Games Platform", fg_color="#343A40", text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=150)
        LoginButton = customtkinter.CTkButton(self, text="Log in", fg_color="#343A40", text_color="#FFFFFF", font=("Roboto", 30, "bold"), border_width=0, height=100, width=300,corner_radius=20,command=self.app.showLoginPanel)
        RegisterButton = customtkinter.CTkButton(self, text="Register", fg_color="#343A40", text_color="#FFFFFF", font=("Roboto", 30, "bold"), border_width=0, height=100, width=300,corner_radius=20,command=self.app.showRegisterPanel)


        TopLabel.pack(fill=customtkinter.X)
        LoginButton.pack(pady=50, padx=50)
        RegisterButton.pack(pady=50, padx=50)
