from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class StockUnit(db.Model, Entity):
    """
    Represents a Product having been bought
    at a Supplier, which can be used to fulfil an OrderProduct.
    """
    __tablename__ = 'stock_unit'

    def __repr__(self):
        return '<StockUnit {id}>'.format(id=self.id)

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship(
        'Product',
        back_populates='stock_units',
    )

    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    supplier = relationship(
        'Supplier',
        back_populates='stock_units',
    )

    packaged_stock_unit = relationship(
        'PackagedStockUnit',
        back_populates='stock_unit',
        uselist=False,
    )

    cost_rands = Column(Numeric, nullable=False)
