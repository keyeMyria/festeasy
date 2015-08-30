from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, UniqueConstraint, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable, Product


class CartProduct(db.Model, Entity, Dumpable):
    __tablename__ = 'cart_product'

    whitelist = [
        'id',
        'created_on',
        'product',
        'quantity',
        'sub_total_rands',
    ]

    def __init__(self, quantity=None, product=None, cart=None):
        self.quantity = quantity
        self.product = product
        self.cart = cart

    def __repr__(self):
        return '<CartProduct {id}>'.format(id=self.id)

    quantity = Column(Integer, default=1, nullable=False)
    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False
    )
    product = relationship(
        'Product',
        back_populates='cart_products',
        cascade='save-update, merge'
    )
    cart_id = Column(
        Integer,
        ForeignKey('cart.id'),
        nullable=False,
    )
    cart = relationship(
        'Cart',
        back_populates='cart_products',
    )
    sub_total_rands = column_property(
        quantity * select([(Product.price_rands)]).where(
            Product.id == product_id
        )
    )

    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id'),
    )
