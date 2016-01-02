from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class CartProduct(db.Model, Entity):
    __tablename__ = 'cart_product'

    def __repr__(self):
        return '<CartProduct {id}>'.format(id=self.id)

    quantity = Column(
        Integer,
        default=1,
        nullable=False,
    )

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

    @property
    def sub_total_rands(self):
        return self.quantity * self.product.price_rands

    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id'),
    )
