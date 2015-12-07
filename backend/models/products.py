from sqlalchemy import Column, String, Numeric
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, ProductPrice


class Product(db.Model, Entity):
    __tablename__ = 'product'

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)

    name = Column(String(150), nullable=False)
    # The cost of a Product in Rands.
    cost_rands = Column(Numeric, nullable=False)
    # Should a Product show up on the products list.
    is_enabled = Column(Boolean, default=False, nullable=False)

    description = Column(String)

    @property
    def price_rands(self):
        product_price = (
            ProductPrice.query
            .filter(ProductPrice.product_id == self.id)
            .order_by(ProductPrice.created_on.desc())
            .first()
        )
        return product_price.amount_rands

    product_prices = relationship(
        'ProductPrice',
        back_populates='product',
    )

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
    invoice_products = relationship(
        'InvoiceProduct',
        back_populates='product',
    )

    categories = relationship(
        'Category',
        secondary='product_category',
        back_populates='products',
    )
