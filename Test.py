import tkinter as tk


main = tk.Tk()
main.title("sadasdasds")
main.geometry("1280x720")
main.resizable(False, False)

TopLabel = tk.Label(text="Games Platform",bg="#343A40",fg="#FFFFFF",font=("Roboto",40,"bold"), height=3)

Submit = tk.Button(main,text="Log in",bg="#343A40",fg="#FFFFFF",font=("Roboto",30,"bold"),borderwidth=0,highlightthickness=0,relief=tk.FLAT,height=1, width=10)

UserNameLabel = tk.Label(text="Username: ",font=("Roboto",20,"bold"))
UsernameEntry = tk.Entry()

PasswordLabel = tk.Label(text="Password: ",font=("Roboto",20,"bold"),)
PasswordEntry = tk.Entry(show="*")

TopLabel.pack(fill=tk.X)

UserNameLabel.pack()
UsernameEntry.pack(pady=10)

PasswordLabel.pack()
PasswordEntry.pack(pady=10)

Submit.pack(pady=50, padx=50)

main.mainloop()