from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.database import Base


class Product_name(Base):
    __tablename__ = 'products_name'

    id = Column(Integer, primary_key=True, nullable=False)
    product_name = Column(String(30), nullable=False)
    product = relationship('Product')
    quantity = Column(Integer)

    def __init__(self, id, product_name, quantity):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity

