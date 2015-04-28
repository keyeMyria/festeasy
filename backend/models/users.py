import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from backend import db
from backend.models import Dumpable


class User(db.Model, Dumpable):
    __tablename__ = 'user'

    whitelist = [
        'created_on',
        'email_address',
    ]

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=False)
    
    email_address = Column(String(200), unique=True, nullable=False)
    sessions = relationship('Session', back_populates="user", cascade='save-update, merge, delete, delete-orphan')

    def __init__(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        return '<User {id}>'.format(id=self.id)
