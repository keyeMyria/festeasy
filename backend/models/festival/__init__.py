from sqlalchemy import Column, String, DateTime
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class Festival(db.Model, Entity):
    __tablename__ = 'festival'

    def __init__(self, is_enabled=None, name=None,
            starts_on=None, ends_on=None, users=[], orders=[]):
        self.name = name
        self.starts_on = starts_on
        self.ends_on = ends_on
        self.users = users
        self.orders = orders

    def __repr__(self):
        return '<Festival {id}>'.format(id=self.id)

    name = Column(String(150), nullable=False)
    starts_on = Column(DateTime)
    ends_on = Column(DateTime)
    is_enabled = Column(Boolean, default=False, nullable=False)

    orders = relationship(
        'Order',
        back_populates='festival',
        cascade='save-update, merge'
    )
    carts = relationship('Cart', back_populates='festival')
