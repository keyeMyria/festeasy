import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Event(db.Model, Entity, Dumpable):
    __tablename__ = 'event'

    whitelist = [
        'id',
        'created_on',
        'name',
    ]
    
    name = Column(String(150), nullable=False)
    starts_on = Column(DateTime)
    ends_on = Column(DateTime)

    users = relationship('User', back_populates='current_cart_event',
        cascade='save-update, merge')

    orders = relationship('Order', back_populates='event',
        cascade='save-update, merge')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Event {id}>'.format(id=self.id)
