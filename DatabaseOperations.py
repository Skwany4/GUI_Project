import sqlite3

conn = sqlite3.connect("Users.db")


c = conn.cursor()

q = "CREATE TABLE IF NOT EXISTS users (id_user INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL,score INTEGER DEFAULT 0)"
q2 = "INSERT INTO Users (email, username, password, score) VALUES ('Szymon@student.com', 'Szymon', '123', 0);"
# try:
#     c.execute(q2)
#     conn.commit()  # Zapisz zmiany w bazie danych
# except sqlite3.IntegrityError:
#     print("Użytkownik o tej nazwie już istnieje.")
q3 = "SELECT * FROM Users"
c.execute(q3)
rows = c.fetchall()  # Pobiera wszystkie rekordy z wynikiem zapytania

# Wyświetlanie danych
for row in rows:
    print(row)

# Zamknięcie połączenia
c.close()
conn.close()
