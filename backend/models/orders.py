import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import relationship, column_property

from backend import db
from backend.models import Entity, Dumpable, OrderProduct


class Order(db.Model, Entity, Dumpable):
    __tablename__ = 'order'

    whitelist = [
        'id',
        'created_on',
        'event',
        'order_products',
        'total_rands',
        'invoices',
    ]
    
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    event = relationship('Event', back_populates='orders',
        cascade='save-update, merge')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='orders',
        cascade='save-update, merge')

    invoices = relationship('Invoice', back_populates='order')

    products = relationship('Product', secondary='order_product', 
        back_populates='orders', cascade='save-update, merge')

    order_products = relationship('OrderProduct', back_populates='order',
        cascade='save-update, merge')

    def __init__(self, event=None, user=None, products=[], order_products=[]):
        self.user = user
        self.products = products
        self.order_products = order_products
        self.event = event

    def from_cart(self, cart):
        with db.session.no_autoflush:
            self.user = cart.user
            self.event = cart.event
            for cart_product in cart.cart_products:
                # TODO: There is an issue with cascade on products and order_products
                self.order_products.append(OrderProduct(
                    product=cart_product.product,
                    quantity=cart_product.quantity,
                    order=self,
                    unit_price_rands=cart_product.product.price_rands,
                    ))

    def __repr__(self):
        return '<Order {id}>'.format(id=self.id)

# Total amount for an Order.
Order.total_rands = column_property(
    select([func.sum(OrderProduct.sub_total_rands)]).where(OrderProduct.order_id==Order.id).correlate(Order)
)
