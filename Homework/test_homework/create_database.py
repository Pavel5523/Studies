# from random import randint
from models.database import create_db, Session
from faker import Faker


def create_database(load_product_data=True):
    create_db()
    if load_product_data:
        _load_product_data(Session())


def _load_product_data(session):
    product_names = ['Огурцы', 'Помидоры', 'Капуста', 'Груши',
                     'Яблоки', 'Клубника', 'Морковь', 'Вишня',
                     'Картофель', 'Малина', 'Бананы']

    for i in product_names:
    product = Product(id=None, product_name=i, quantity=None)
    session.add(product)



    session.commit()
    session.close()
