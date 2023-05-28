import os
from models.database import DATABASE_NAME, Session
import create_database as db_creator
# from model.product import Product
# from model.product_name import Product_name

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
