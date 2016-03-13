from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class ProductSupplier(db.Model, Entity):
    """
    Represents a Supplier offering a Product.
    """
    __tablename__ = 'product_supplier'

    cost_rands = Column(Numeric)

    product_id = Column(
        Integer,
        ForeignKey('product.id'),
        nullable=False,
    )
    product = relationship(
        'Product',
        back_populates='product_suppliers',
    )

    supplier_id = Column(
        Integer,
        ForeignKey('supplier.id'),
        nullable=False,
    )
    supplier = relationship(
        'Supplier',
        back_populates='product_suppliers',
    )
