from sqlalchemy import Column, String, Integer, ForeignKey
from model.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    category = Column(String(30), ForeignKey('products_name.id'),  nullable=False)

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f'Категория продукта: {self.category}'
