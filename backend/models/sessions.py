import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity


class Session(db.Model, Entity):
    __tablename__ = 'session'
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='sessions', cascade='save-update, merge')
    expires_on = Column(DateTime, nullable=False)

    def __init__(self, expires_on):
        self.expires_on = expires_on

    def __repr__(self):
        return '<Session {id}>'.format(id=self.id)
