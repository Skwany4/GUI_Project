import sqlite3

conn = sqlite3.connect("Users.db")

c = conn.cursor()

# c.execute("""CREATE TABLE users (
#             username TEXT,
#             password TEXT,
#             email TEXT
# )""")

# c.execute("INSERT INTO users VALUES ('Szymon','123','Szymon@gmail.com')")

c.execute("SELECT * FROM users")

print(c.fetchone() )
conn.commit()

conn.close()