from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, UniqueConstraint, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Product


class CartProduct(db.Model, Entity):
    __tablename__ = 'cart_product'

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
