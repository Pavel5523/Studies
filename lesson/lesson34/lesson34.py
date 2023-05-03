import sqlite3

# con = sqlite3.connect('profile.db')
# cur = con.cursor()
#
# cur.execute('''''')
#
# con.close()

# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date TEXT
#     )''')

with sqlite3.connect('users.db') as con:
    cur = con.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS person(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     phone BLOB NOT NULL DEFAULT "+79090000000",
    #     age INTEGER CHECK(age > 0 AND age < 100),
    #     email TEXT UNIQUE
    # )''')
    #
    # cur.execute('''
    # ALTER TABLE person
    # RENAME TO person_table
    # ''')

    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN addres TEXT NOT NULL DEFAULT 'city, address'
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address
    # """)

    # cur.execute("""
    #     ALTER TABLE person_table
    #     DROP COLUMN address home_address
    #     """)

    # cur.execute("""
    #     DROP TABLE person_table
    #     """)