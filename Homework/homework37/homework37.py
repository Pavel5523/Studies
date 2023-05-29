import sqlite3

laptops = [
    ('Asus', '17"', 23400),
    ('Acer', '17"', 22500),
    ('Dell', '15,6"', 25200),
    ('Lenovo', '14"', 28300),
    ('HP', '15,6"', 23800),
    ('Samsung', '17"', 29400),
    ('MSI', '17"', 26000),
]

with sqlite3.connect('laptops.db') as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE  IF NOT EXISTS laptops(
        laptop_id INTEGER PRIMARY KEY AUTOINCREMENT,
        models TEXT,
        size TEXT,
        price INTEGER
    )
    ''')

    cur.executemany('INSERT INTO laptops VALUES(NULL, ?, ?, ?)', laptops)
