from sqlalchemy import Column, String, Numeric
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class Product(db.Model, Entity):
    __tablename__ = 'product'

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

    name = Column(String(150), nullable=False)
    # The price of a Product in Rands.
    price_rands = Column(Numeric, nullable=False)
    # The cost of a Product in Rands.
    cost_rands = Column(Numeric, nullable=False)
    # Should a Product show up on the products list.
    is_enabled = Column(Boolean, default=False, nullable=False)

    description = Column(String)

    carts = relationship(
        'Cart',
        secondary='cart_product',
        back_populates='products',
        cascade='save-update, merge'
    )
    cart_products = relationship(
        'CartProduct',
        back_populates='product',
        cascade='save-update, merge, delete'
    )

    orders = relationship(
        'Order',
        secondary='order_product',
        back_populates='products',
        cascade='save-update, merge'
    )
    order_products = relationship(
        'OrderProduct',
        back_populates='product',
        cascade='save-update, merge'
    )

    invoices = relationship(
        'Invoice',
        secondary='invoice_product',
        back_populates='products',
    )
    invoice_products = relationship('InvoiceProduct', back_populates='product')
