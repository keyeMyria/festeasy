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

    token = Column(String(200), nullable=False, unique=True)

    def __init__(self, expires_on, token, user=None):
        self.expires_on = expires_on
        self.user = user
        self.token = token

    def __repr__(self):
        return '<Session {id}>'.format(id=self.id)
