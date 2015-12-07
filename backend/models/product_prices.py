from sqlalchemy import Column, Numeric, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class ProductPrice(db.Model, Entity):
    __tablename__ = 'product_price'

    def __repr__(self):
        return '<ProductPrice {id}>'.format(id=self.id)

    amount_rands = Column(Numeric)
    info = Column(String)

    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False,
    )
    product = relationship(
        'Product',
        back_populates='product_prices',
    )
