from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Homework.homework38.model.database import Base


class Product(Base):
    __tablename__ = 'products_name'

    id = Column(Integer, primary_key=True, nullable=False)
    product_name = Column(String(30), nullable=False)
    product = relationship('Product')
    quantity = Column(Integer)

    def __init__(self, id, product_name, quantity):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity

    def __repr__(self):
        return f'Название продукта: {self.product_name}, Количество продукта: {self.quantity}'
