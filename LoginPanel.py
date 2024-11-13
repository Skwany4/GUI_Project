import tkinter
import customtkinter
from PIL import Image, ImageTk
import sqlite3


class LoginPanel(tkinter.Frame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createLoginPanel()

    def createLoginPanel(self):
        TopLabel = customtkinter.CTkLabel(self, text="Games Platform", fg_color="#343A40",
                                          text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=150)

        Submit = customtkinter.CTkButton(self, text="Log in", fg_color="#343A40", text_color="#FFFFFF",
                                         corner_radius=20, font=("Roboto", 30, "bold"), height=100, width=300,
                                         command=self.verify_login)

        self.BackArrowImage = customtkinter.CTkImage(Image.open("Images/BackArrow.png"), size=(50, 50))
        BackButton = customtkinter.CTkButton(self, image=self.BackArrowImage, text="", fg_color="#FFFFFF",
                                             hover=False, command=self.app.showMainMenu)

        UserNameLabel = customtkinter.CTkLabel(self, text="Username: ", font=("Roboto", 20, "bold"), text_color="#000000")
        self.UsernameEntry = customtkinter.CTkEntry(self)

        PasswordLabel = customtkinter.CTkLabel(self, text="Password: ", font=("Roboto", 20, "bold"),text_color="#000000")
        self.PasswordEntry = customtkinter.CTkEntry(self, show="*")

        self.message_label = customtkinter.CTkLabel(self, text="", text_color="red", font=("Roboto", 16))

        TopLabel.pack(fill=tkinter.X)

        UserNameLabel.pack()
        self.UsernameEntry.pack(pady=10)

        PasswordLabel.pack()
        self.PasswordEntry.pack(pady=10)

        Submit.pack(pady=50, padx=50)
        self.message_label.pack()

        BackButton.pack(pady=10, padx=10, side="left")

    def verify_login(self):
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        conn = sqlite3.connect("Users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            self.message_label.configure(text="Login successful!", text_color="green")
            self.app.showSelectGame()
        else:
            self.message_label.configure(text="Invalid username or password", text_color="red")
            self.UsernameEntry.delete(0, tkinter.END)
            self.PasswordEntry.delete(0, tkinter.END)

        conn.close()
