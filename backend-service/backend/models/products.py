from sqlalchemy import Column, String, Numeric, Boolean
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Product(db.Model, Entity):
    def __repr__(self):
        return '<Product {self.id}>'.format(self=self)

    # Estimated cost of a product. Actual cost is recorded on a StockUnit.
    cost_rands = Column(Numeric)
    description = Column(String)
    # Should a Product show up on the products list.
    is_enabled = Column(Boolean, default=False, nullable=False)
    name = Column(String(150), nullable=False)
    price_rands = Column(Numeric, nullable=False)

    cart_products = relationship(
        'CartProduct',
        back_populates='product',
        cascade='save-update, merge, delete, delete-orphan'
    )

    invoice_products = relationship(
        'InvoiceProduct',
        back_populates='product',
    )

    order_products = relationship(
        'OrderProduct',
        back_populates='product',
    )

    product_categories = relationship(
        'ProductCategory',
        back_populates='product',
    )

    stock_units = relationship(
        'StockUnit',
        back_populates='product',
    )
