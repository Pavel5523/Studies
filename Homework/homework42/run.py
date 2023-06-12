from flask import Flask, render_template, g
import os
import sqlite3
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'dbaea81d62ca46416fe667572ce4d8f3c4fc4128'
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


@app.route('/')
# @app.route('/index')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title='Главная', menu=dbase.get_menu(), prewie='Содержимое главной страницы')


@app.route('/second')
def second():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('second.html', title='Вторая страница', menu=dbase.get_menu(),
                           prewie='Содержимое второй страницы')


@app.route('/third')
def third():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('third.html', title='Третья страница', menu=dbase.get_menu(),
                           prewie='Содержимое третьей страницы')


@app.route('/fourth')
def fourth():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('fourth.html', title='Четвертая страница', menu=dbase.get_menu(),
                           prewie='Содержимое четвертой страницы')


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title='Страница не найдена', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
