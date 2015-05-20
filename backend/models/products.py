import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Product(db.Model, Entity, Dumpable):
    __tablename__ = 'product'

    whitelist = [
        'id',
        'created_on',
        'name',
        'price_cents',
    ]
    
    name = Column(String(150), nullable=False)
    price_cents = Column(Integer, nullable=False)

    cart_users = relationship('User', secondary='user_cart_product',
        cascade='save-update, merge')

    user_cart_products = relationship('UserCartProduct',
        cascade='save-update, merge, delete, delete-orphan')

    orders = relationship('Order', secondary='order_product',
        cascade='save-update, merge')

    def __init__(self, name, price_cents):
        self.name = name
        self.price_cents = price_cents

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)
