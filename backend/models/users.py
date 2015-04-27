from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from backend import db
from backend.models import Entity


class User(db.Model, Entity):
	__tablename__ = 'user'
	email_address = Column(String(200), unique=True, nullable=False)
	sessions = relationship('Session', back_populates="user", cascade='save-update, merge, delete, delete-orphan')
	def __init__(self, email_address):
		self.email_address = email_address
