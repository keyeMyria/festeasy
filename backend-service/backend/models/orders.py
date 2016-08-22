from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from backend import db

from . import OrderProduct
from .utils import Entity
from .invoices import Invoice


class Order(db.Model, Entity):
    def __repr__(self):
        return '<Order {self.id}>'.format(self=self)

    festival_id = Column(ForeignKey('festival.id'), nullable=False)
    festival = relationship(
        'Festival',
        back_populates='orders',
    )

    user_id = Column(ForeignKey('user.id'), nullable=False)
    user = relationship(
        'User',
        back_populates='orders',
        cascade='save-update, merge'
    )

    shipping_address = Column(String)

    invoices = relationship(
        'Invoice',
        back_populates='order',
    )

    order_products = relationship(
        'OrderProduct',
        back_populates='order',
    )

    packages = relationship(
        'Package',
        back_populates='order',
    )

    collection = relationship(
        'Collection',
        back_populates='order',
        uselist=False,
    )

    # TODO: Test.
    @property
    def current_invoice(self):
        return (Invoice.query
                .filter(Invoice.order_id == self.id)
                .order_by(Invoice.created_on.desc())
                .first())

    # TODO: Imporve testing
    @staticmethod
    def from_cart(cart):
        if not cart.festival:
            raise Exception('Cart does not have a Festival.')
        if cart.cart_products == []:
            raise Exception('Cart does not have any CartProducts.')
        order = Order()
        order.user = cart.user
        order.festival = cart.festival
        for cart_product in cart.cart_products:
            # TODO: There is an issue with cascade
            # on products and order_products
            order.order_products.append(
                OrderProduct(
                    product=cart_product.product,
                    order=order,
                    quantity=cart_product.quantity,
                    unit_price_rands=cart_product.product.price_rands,
                )
            )
        return order

    @property
    def total_rands(self):
        total = 0
        for op in self.order_products:
            total += op.sub_total_rands
        return total
