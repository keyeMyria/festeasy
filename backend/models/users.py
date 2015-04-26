from sqlalchemy import Column, Integer, String

from backend import db


class User(db.Model):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	email_address = Column(String(200), unique=True, nullable=False)
