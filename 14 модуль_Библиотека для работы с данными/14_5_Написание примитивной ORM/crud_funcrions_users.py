import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )""")
    connection.commit()
    connection.close()

def add_user(username, email, age):
    cursor.execute("SELECT COUNT(*) FROM Users")
    total_users = cursor.fetchone()[0] + 1
    cursor.execute(f'''
            INSERT INTO Users VALUES('{total_users}', '{username}', '{email}', '{age}', '1000')
            ''')
    connection.commit()
    connection.close()

def is_included(username):
    cursor = connection.cursor()
    user_in = True
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user.fetchone() is None:
        user_in = False
    return user_in
    connection.commit()
    connection.close()

