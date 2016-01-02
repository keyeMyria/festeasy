from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class ProductStock(db.Model, Entity):
    """
    Represents a Product having been bought
    at a Supplier, which can be used to fulfil an OrderProduct.
    """
    __tablename__ = 'product_stock'

    def __repr__(self):
        return '<ProductStock {id}>'.format(id=self.id)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship(
        'Product',
        back_populates='product_stocks',
    )

    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    supplier = relationship(
        'Supplier',
        back_populates='product_stocks',
    )

    cost_rands = Column(Numeric, nullable=False)
