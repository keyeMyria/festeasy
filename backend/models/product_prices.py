from sqlalchemy import Column, Numeric, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class ProductPrice(db.Model, Entity):
    """
    Represents the retail price for a Product.
    """
    __tablename__ = 'product_price'

    def __repr__(self):
        return '<ProductPrice {id}>'.format(id=self.id)

    amount_rands = Column(Numeric)
    notes = Column(String)

    # TODO: Implement ProductPrice coming into effect after date.
    # effective_from = Column(Datetime)

    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False,
    )
    product = relationship(
        'Product',
        back_populates='product_prices',
    )
