import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Order(db.Model, Entity, Dumpable):
    __tablename__ = 'order'

    whitelist = [
        'id',
        'created_on',
        'event',
        'user',
    ]
    
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    event = relationship('Event', back_populates='orders',
        cascade='save-update, merge')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='orders',
        cascade='save-update, merge')

    def __init__(self):
        pass

    def __repr__(self):
        return '<Order {id}>'.format(id=self.id)
