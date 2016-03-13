from sqlalchemy import Column, String, Numeric
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db

from .utils import Entity


class Product(db.Model, Entity):
    __tablename__ = 'product'

    def __init__(self, cost_rands=None, description=None, is_enabled=False,
                 name=None, price_rands=None, product_categories=None,
                 suppliers=None):
        self.cost_rands = cost_rands
        self.description = description
        self.is_enabled = is_enabled
        self.name = name
        self.price_rands = price_rands
        if product_categories:
            self.product_categories = product_categories
        if suppliers:
            self.suppliers = suppliers

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

    # The cost of a Product in Rands.
    cost_rands = Column(Numeric)
    description = Column(String)
    # Should a Product show up on the products list.
    is_enabled = Column(Boolean, default=False, nullable=False)
    name = Column(String(150), nullable=False)
    price_rands = Column(Numeric, nullable=False)

    cart_products = relationship(
        'CartProduct',
        back_populates='product',
        cascade='save-update, merge, delete'
    )

    invoice_products = relationship(
        'InvoiceProduct',
        back_populates='product',
    )

    order_products = relationship(
        'OrderProduct',
        back_populates='product',
        cascade='save-update, merge'
    )

    product_categories = relationship(
        'ProductCategory',
        back_populates='product',
    )

    stock_units = relationship(
        'StockUnit',
        back_populates='product',
    )

    suppliers = relationship(
        'Supplier',
        secondary='product_supplier',
        back_populates='products',
    )
