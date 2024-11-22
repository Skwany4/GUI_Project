import tkinter
import customtkinter
from PIL import Image, ImageTk
import sqlite3


class RegisterPanel(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app
        self.configure(fg_color="#0D1321")  # Background color
        self.createRegisterPanel()


    def createRegisterPanel(self):
        RegisterFrame = customtkinter.CTkFrame(self, corner_radius=50, fg_color="#1D2D44", width=600, height=600)
        RegisterFrame.grid_propagate(False)

        self.update_idletasks()
        print(RegisterFrame.winfo_width(), RegisterFrame.winfo_height())

        RegisterFrame.grid_columnconfigure(0, weight=1)
        RegisterFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12), weight=1)

        TopLabel = customtkinter.CTkLabel(RegisterFrame, text="Register", font=("Roboto", 40, "bold"),
                                          text_color="#FFFFFF")

        logoImage = customtkinter.CTkImage(Image.open("Menu/Images/Logo.png"), size=(400, 100))
        logoLabel = customtkinter.CTkLabel(RegisterFrame, text="", image=logoImage)

        EmailLabel = customtkinter.CTkLabel(RegisterFrame, text="Email: ", font=("Roboto", 20), text_color="#FFFFFF")
        self.EmailEntry = customtkinter.CTkEntry(RegisterFrame)

        UserNameLabel = customtkinter.CTkLabel(RegisterFrame, text="Username: ", font=("Roboto", 20),
                                               text_color="#FFFFFF")
        self.UsernameEntry = customtkinter.CTkEntry(RegisterFrame)

        PasswordLabel = customtkinter.CTkLabel(RegisterFrame, text="Password: ", font=("Roboto", 20),
                                               text_color="#FFFFFF")
        self.PasswordEntry = customtkinter.CTkEntry(RegisterFrame, show="*")

        ConfirmPasswordLabel = customtkinter.CTkLabel(RegisterFrame, text="Confirm password: ", font=("Roboto", 20),
                                                      text_color="#FFFFFF")
        self.ConfirmPasswordEntry = customtkinter.CTkEntry(RegisterFrame, show="*")

        self.ConfirmCheckBox = customtkinter.CTkCheckBox(RegisterFrame, text="I agree to the terms and conditions",
                                                         text_color="#FFFFFF", width=50, height=50)

        Submit = customtkinter.CTkButton(RegisterFrame, text="Register", fg_color="#3E5C76", text_color="#FFFFFF",
                                         corner_radius=25, font=("Roboto", 30, "bold"), height=100, width=300,
                                         command=self.registerUser)

        self.message_label = customtkinter.CTkLabel(self, text="", text_color="red", font=("Roboto", 16))

        logoLabel.grid(row=1, column=0, pady=20)
        EmailLabel.grid(row=2, column=0, padx=20, pady=5)
        self.EmailEntry.grid(row=3, column=0, padx=20, pady=10)
        UserNameLabel.grid(row=4, column=0, padx=20, pady=5)
        self.UsernameEntry.grid(row=5, column=0, padx=20, pady=10)
        PasswordLabel.grid(row=6, column=0, padx=20, pady=5)
        self.PasswordEntry.grid(row=7, column=0, padx=20, pady=10)
        ConfirmPasswordLabel.grid(row=8, column=0, padx=20, pady=5)
        self.ConfirmPasswordEntry.grid(row=9, column=0, padx=20, pady=10)
        self.ConfirmCheckBox.grid(row=10, column=0, padx=20, pady=10)
        Submit.grid(row=12, column=0, padx=20, pady=10)

        self.message_label.grid(row=12, column=0, padx=20, pady=10)

        RegisterFrame.grid(row=0, column=0, padx=20, pady=20)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.BackArrowImage = customtkinter.CTkImage(Image.open("Menu/Images/BackArrow.png"), size=(50, 50))
        BackButton = customtkinter.CTkButton(self, image=self.BackArrowImage, text="", fg_color="transparent",
                                             hover=False, command=self.app.showMainMenu)
        BackButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    def registerUser(self):
        email = self.EmailEntry.get()
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()
        confirmPassword = self.ConfirmPasswordEntry.get()
        confirmed = self.ConfirmCheckBox.get()

        if not email or not username or not password or not confirmPassword:
            self.message_label.configure(text="All fields must be filled.", text_color="red")
            return
        if password != confirmPassword:
            self.message_label.configure(text="Passwords do not match", text_color="red")
            return
        if not confirmed:
            self.message_label.configure(text="Please confirm registration.", text_color="red")
            return

        conn = sqlite3.connect("Menu/Users.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (email, username, password, score) VALUES (?, ?, ?, ?)",
                           (email, username, password, 0))
            conn.commit()
            self.message_label.configure(text="Registration successful!", text_color="green")
            self.app.showMainMenu()
        except sqlite3.IntegrityError:
            self.message_label.configure(text="Username or email already exists.", text_color="red")
        finally:
            cursor.close()
            conn.close()
