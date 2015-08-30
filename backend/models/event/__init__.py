from sqlalchemy import Column, String, DateTime
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Event(db.Model, Entity, Dumpable):
    __tablename__ = 'event'

    whitelist = [
        'id',
        'created_on',
        'name',
        'starts_on',
        'ends_on',
        'is_enabled',
    ]

    def __init__(self, is_enabled=None, name=None,
            starts_on=None, ends_on=None, users=[], orders=[]):
        self.is_enabled = is_enabled
        self.name = name
        self.starts_on = starts_on
        self.ends_on = ends_on
        self.users = users
        self.orders = orders

    def __repr__(self):
        return '<Event {id}>'.format(id=self.id)

    name = Column(String(150), nullable=False)
    starts_on = Column(DateTime)
    ends_on = Column(DateTime)
    is_enabled = Column(Boolean, default=False, nullable=False)

    orders = relationship(
        'Order',
        back_populates='event',
        cascade='save-update, merge'
    )
    carts = relationship('Cart', back_populates='event')
