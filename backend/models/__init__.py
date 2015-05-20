import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime

from backend import db


class Dumpable(object):
    whitelist = []
    def dump(self):
        return {attr: getattr(self, attr) 
            for attr in self.whitelist}

class Entity(object):
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.datetime.now, 
        nullable=False)

# All the models
from sessions import Session
from users import User
from products import Product
from user_cart_products import UserCartProduct
from events import Event
from orders import Order
