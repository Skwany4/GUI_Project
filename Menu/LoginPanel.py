import tkinter
import customtkinter
from PIL import Image, ImageTk
import sqlite3


class LoginPanel(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createLoginPanel()
        self.configure(fg_color="#0D1321")

    def createLoginPanel(self):
        LoginFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=600)
        LoginFrame.grid_propagate(False)

        LoginFrame.grid_columnconfigure(0, weight=1)
        LoginFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        logoImage = customtkinter.CTkImage(Image.open("Menu/Images/Logo.png"), size=(400, 100))
        logoLabel = customtkinter.CTkLabel(LoginFrame, text="", image=logoImage)

        UserNameLabel = customtkinter.CTkLabel(LoginFrame, text="Username: ", font=("Roboto", 20), text_color="#FFFFFF")
        self.UsernameEntry = customtkinter.CTkEntry(LoginFrame)

        PasswordLabel = customtkinter.CTkLabel(LoginFrame, text="Password: ", font=("Roboto", 20), text_color="#FFFFFF")
        self.PasswordEntry = customtkinter.CTkEntry(LoginFrame, show="*")

        Submit = customtkinter.CTkButton(LoginFrame, text="Log in", fg_color="#3E5C76", text_color="#FFFFFF", corner_radius=25, font=("Roboto", 30, "bold"), height=100, width=300, command=self.verify_login)

        self.message_label = customtkinter.CTkLabel(self, text="", text_color="red", font=("Roboto", 16))

        logoLabel.grid(row=0, column=0, pady=20)
        UserNameLabel.grid(row=1, column=0, padx=20, pady=10)
        self.UsernameEntry.grid(row=2, column=0, padx=20, pady=10)
        PasswordLabel.grid(row=3, column=0, padx=20, pady=10)
        self.PasswordEntry.grid(row=4, column=0, padx=20, pady=10)
        Submit.grid(row=5, column=0, padx=20, pady=20)
        self.message_label.grid(row=6, column=0, padx=20, pady=10)

        LoginFrame.grid(row=0, column=0, padx=20, pady=20)


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.BackArrowImage = customtkinter.CTkImage(Image.open("Menu/Images/BackArrow.png"), size=(50, 50))
        BackButton = customtkinter.CTkButton(self, image=self.BackArrowImage, text="", fg_color="transparent", hover=False, command=self.app.showMainMenu)
        BackButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Back button at the top left

    def verify_login(self):
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        conn = sqlite3.connect("Menu/Users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            self.message_label.configure(text="Login successful!", text_color="green")
            userId = result[0]
            self.app.loggedUserId = userId
            self.app.showSelectGame()
        else:
            self.message_label.configure(text="Invalid username or password", text_color="red")
            self.UsernameEntry.delete(0, tkinter.END)
            self.PasswordEntry.delete(0, tkinter.END)

        conn.close()
