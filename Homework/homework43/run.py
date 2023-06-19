from flask import Flask, render_template, g, request, session, redirect, flash
import os
import sqlite3
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '94aab7e44b1c3de445da94ba3ee42efeaac4ec46'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/', methods=['POST', 'GET'])
def index():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        res = dbase.add_product(request.form['title'])
        if not res:
            flash('Ошибка добавления товара', category='error')
        else:
            flash('Товар добавлен в корзину', category='success')
    return render_template('index.html', menu=dbase.get_menu(), title='Главная страница')


@app.route('/info')
def info_prod():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('info.html', menu=dbase.get_menu(), title='Информация о товаре')


@app.route('/first_prod', methods=['POST', 'GET'])
def first_prod():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        res = dbase.add_product(request.form['title'])
        if not res:
            flash('Ошибка добавления товара', category='error')
        else:
            flash('Товар добавлен в корзину', category='success')
    return render_template('first_prod.html', menu=dbase.get_menu(), title='Первый товар')


@app.route('/second_prod', methods=['POST', 'GET'])
def second_prod():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        res = dbase.add_product(request.form['title'])
        if not res:
            flash('Ошибка добавления товара', category='error')
        else:
            flash('Товар добавлен в корзину', category='success')
    return render_template('second_prod.html', menu=dbase.get_menu(), title='Второй товар')


@app.route('/third_prod', methods=['POST', 'GET'])
def third_prod():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        res = dbase.add_product(request.form['title'])
        if not res:
            flash('Ошибка добавления товара', category='error')
        else:
            flash('Товар добавлен в корзину', category='success')
    return render_template('third_prod.html', menu=dbase.get_menu(), title='Третий товар')


@app.route('/trash', methods=['POST', 'GET'])
def trash():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        dbase.del_prod()
    return render_template('trash.html', menu=dbase.get_menu(), prod=dbase.get_prod())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
