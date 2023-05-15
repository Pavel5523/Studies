import sqlite3
with sqlite3.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 5 OFFSET 2;
    ''')

    # res = cur.fetchall()
    # print(res)
    # for res in cur:
    #     print(res)
    # res = cur.fetchone()
    # print(res)
    # res = cur.fetchmany(2)
    # print(res)
    # for res in cur:
    #     print(res)
