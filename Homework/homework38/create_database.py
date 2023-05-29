from random import randint
from model.database import create_db, Session
from model.product import Product
from model.product_name import Product_name


def create_database(load_product_data=True):
    create_db()
    if load_product_data:
        _load_product_data(Session())


def _load_product_data(session):
    product_names = ['Огурцы', 'Помидоры', 'Капуста', 'Груши',
                     'Яблоки', 'Клубника', 'Морковь', 'Вишня',
                     'Картофель', 'Малина', 'Бананы']
    for i in range(len(product_names)):
        random_quantity = randint(10, 250)
        product = Product_name(id=None, product_name=product_names[i], quantity=random_quantity)
        session.add(product)
    session.commit()

    category1 = Product(category='Овощи')
    category2 = Product(category='Фрукты')
    category3 = Product(category='Ягоды')
    session.add(category1)
    session.add(category2)
    session.add(category3)

    session.commit()
    session.close()
