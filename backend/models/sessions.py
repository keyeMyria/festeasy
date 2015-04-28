import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Entity, Dumpable


class Session(db.Model, Entity, Dumpable):
    __tablename__ = 'session'

    whitelist = [
    	'created_on',
    	'expires_on',
    ]
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='sessions', 
    	cascade='save-update, merge')
    expires_on = Column(DateTime, nullable=False)

    def __init__(self, expires_on, user):
        self.expires_on = expires_on
        self.user = user

    def __repr__(self):
        return '<Session {id}>'.format(id=self.id)
