from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db

from . import OrderProduct
from .utils import Entity


class Order(db.Model, Entity):
    __tablename__ = 'order'

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

    def __repr__(self):
        return '<Order {id}>'.format(id=self.id)

    festival_id = Column(Integer, ForeignKey('festival.id'), nullable=False)
    festival = relationship(
        'Festival',
        back_populates='orders',
        cascade='save-update, merge'
    )

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(
        'User',
        back_populates='orders',
        cascade='save-update, merge'
    )

    invoices = relationship(
        'Invoice',
        back_populates='order',
    )

    order_products = relationship(
        'OrderProduct',
        back_populates='order',
        cascade='save-update, merge'
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

    @property
    def total_rands(self):
        total = 0
        for op in self.order_products:
            total += op.sub_total_rands
        return total
