from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Вторая страница', 'url': 'second'},
    {'name': 'Третья страница', 'url': 'third'},
    {'name': 'Четвертая страница', 'url': 'fourth'},
]


@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/second')
def second():
    return render_template('second.html', title='Вторая страница', menu=menu)


@app.route('/third')
def third():
    return render_template('third.html', title='Третья страница', menu=menu)


@app.route('/fourth')
def fourth():
    return render_template('fourth.html', title='Четвертая страница', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
