import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка базы данных')
        return []

    def add_product(self, title):
        try:
            self.__cur.execute('INSERT INTO products VALUES(NULL, ?)', (title,))
            self.__db.commit()
        except sqlite3.Error:
            print('Ошибка добавления товара в корзину')
            return False
        return True

    def get_prod(self):
        try:
            self.__cur.execute("SELECT * FROM products")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения товара из БД " + str(e))
        return []

    def del_prod(self):
        self.__cur.execute('DELETE FROM products')
        self.__db.commit()
        return 
