import sqlite3
import customtkinter

class Profile(customtkinter.CTkFrame):
    def __init__(self, app, userId):
        super().__init__(app.tk)
        self.app = app
        self.userId = userId
        self.configure(fg_color="#1D2D44")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.createProfile()
        self.loadUser()

    def createProfile(self):
        header_label = customtkinter.CTkLabel(self.main_frame,text="User Profile",font=("Roboto", 30, "bold"),text_color="#FFFFFF",)
        header_label.grid(row=0, column=0, pady=(20, 10))

        user_frame = customtkinter.CTkFrame(self.main_frame,fg_color="#343A40",corner_radius=20,width=400,height=250)
        user_frame.grid(row=1, column=0, pady=20, padx=20, sticky="n")
        user_frame.grid_propagate(False)
        user_frame.grid_rowconfigure((0, 1, 2), weight=1)
        user_frame.grid_columnconfigure(0, weight=1)

        self.username_label = customtkinter.CTkLabel(user_frame,text="Username: ",font=("Roboto", 18),text_color="#FFFFFF",)
        self.username_label.grid(row=0, column=0, pady=5, sticky="w", padx=10)

        self.email_label = customtkinter.CTkLabel(user_frame,text="Email: ",font=("Roboto", 18),text_color="#FFFFFF",)
        self.email_label.grid(row=1, column=0, pady=5, sticky="w", padx=10)

        self.score_label = customtkinter.CTkLabel(user_frame,text="Score: ",font=("Roboto", 18),text_color="#FFFFFF")
        self.score_label.grid(row=2, column=0, pady=5, sticky="w", padx=10)

        back_button = customtkinter.CTkButton(self.main_frame,text="Back to Menu",font=("Roboto", 16, "bold"),fg_color="#3E5C76",text_color="#FFFFFF",hover_color="#5A7E99",corner_radius=25,command=self.app.showSelectGame,)
        back_button.grid(row=2, column=0, pady=20)

    def loadUser(self):
        try:
            conn = sqlite3.connect('Menu/Users.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT username, email, score FROM users WHERE id_user = ?",
                (self.userId,),
            )
            user_data = cursor.fetchone()

            conn.close()

            if user_data:
                self.username_label.configure(text=f"Username: {user_data[0]}")
                self.email_label.configure(text=f"Email: {user_data[1]}")
                self.score_label.configure(text=f"Score: {user_data[2]}")
            else:
                self.username_label.configure(text="Username: Not Found")
                self.email_label.configure(text="Email: Not Found")
                self.score_label.configure(text="Score: 0")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
