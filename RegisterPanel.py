import tkinter
import customtkinter
from PIL import Image, ImageTk
import sqlite3

class RegisterPanel(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.createRegisterPanel()

    def createRegisterPanel(self):

        TopLabel = customtkinter.CTkLabel(self,text="Games Platform", fg_color="#343A40", text_color="#FFFFFF", font=("Roboto", 40, "bold"), height=150)

        EmailLabel = customtkinter.CTkLabel(self, text="Email: ", font=("Roboto", 20, "bold"),text_color="#000000")
        self.EmailEntry = customtkinter.CTkEntry(self)

        UserNameLabel = customtkinter.CTkLabel(self, text="Username: ", font=("Roboto", 20, "bold"),text_color="#000000")
        self.UsernameEntry = customtkinter.CTkEntry(self)

        PasswordLabel = customtkinter.CTkLabel(self, text="Password: ", font=("Roboto", 20, "bold"), text_color="#000000")
        self.PasswordEntry = customtkinter.CTkEntry(self, show="*")

        ConfirmPasswordLabel = customtkinter.CTkLabel(self,text="Confirm password: ", font=("Roboto", 20, "bold"),text_color="#000000")
        self.ConfrimPasswordEntry = customtkinter.CTkEntry(self,show="*")

        self.ConfirmCheckBox = customtkinter.CTkCheckBox(self, text="Confirm",text_color="#000000")

        Submit = customtkinter.CTkButton(self, text="Register", fg_color="#343A40", text_color="#FFFFFF",
                                         corner_radius=20, font=("Roboto", 30, "bold"), height=100, width=300,
                                         command=self.registerUser)

        self.BackArrowImage = customtkinter.CTkImage(Image.open("Images/BackArrow.png"), size=(50, 50))

        BackButton = customtkinter.CTkButton(self, image=self.BackArrowImage, text="", fg_color="#FFFFFF", hover=False,
                                             command=self.app.showMainMenu,)

        self.MessageLabel = customtkinter.CTkLabel(self, text ="")


        TopLabel.pack(fill=tkinter.X)
        
        EmailLabel.pack()
        self.EmailEntry.pack(pady=10)

        UserNameLabel.pack()
        self.UsernameEntry.pack(pady=10)

        PasswordLabel.pack()
        self.PasswordEntry.pack(pady=10)

        ConfirmPasswordLabel.pack()
        self.ConfrimPasswordEntry.pack(pady=10)

        self.ConfirmCheckBox.pack()

        Submit.pack()

        self.MessageLabel.pack()

        BackButton.pack(pady = 10, padx = 10, side="left")


    def registerUser(self):
            email = self.EmailEntry.get()
            username = self.UsernameEntry.get()
            password = self.PasswordEntry.get()
            confirmPassword = self.ConfrimPasswordEntry.get()
            confirmed = self.ConfirmCheckBox.get()

            if not email or not username or not password or not confirmPassword:
                self.MessageLabel.configure(text="All fields must be filled. ")
                return
            if password != confirmPassword:
                self.MessageLabel.configure(text="Passwords do not match")
                return
            if not confirmed:
                self.MessageLabel.configure(text="Please confirm registration.", text_color="red")
                return

            conn = sqlite3.connect("Users.db")
            cursor = conn.cursor()

            try:
                cursor.execute("INSERT INTO users (email, username, password, score) VALUES (?, ?, ?, ?)",
                           (email, username, password, 0))
                conn.commit()
                self.MessageLabel.configure(text="Registration successful!", text_color="green")
                self.app.showMainMenu()
            except sqlite3.IntegrityError:
                self.MessageLabel.configure(text="Username or email already exists.", text_color="red")
            finally:
                cursor.close()
                conn.close()