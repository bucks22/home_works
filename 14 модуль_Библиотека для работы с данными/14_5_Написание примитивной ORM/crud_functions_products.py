import sqlite3

connection = sqlite3.connect('tg_bot.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )""")
    connection.commit()

initiate_db()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products
    connection.commit()
    connection.close()

for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Product{i}',
                                                                                             f'Описание товара {i}',
                                                                                             i*1432))