from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from backend import db

from .utils import Entity


class Supplier(db.Model, Entity):
    """
    A supplier is a physical store from where Products
    are bought.
    EG: Woolies in Palmyra Junction.
    """
    __tablename__ = 'supplier'

    def __repr__(self):
        return '<Supplier {id}>'.format(id=self.id)

    name = Column(String)
    location = Column(String)
    contact_numer = Column(String)

    base_supplier_id = Column(
        Integer,
        ForeignKey('base_supplier.id'),
        )
    base_supplier = relationship(
        'BaseSupplier',
        back_populates="suppliers",
    )

    products = relationship(
        'Product',
        secondary='product_supplier',
        back_populates='suppliers',
    )

    stock_units = relationship(
        'StockUnit',
        back_populates='supplier',
    )
