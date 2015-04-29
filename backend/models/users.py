import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from backend import db
from backend.models import Entity, Dumpable


class User(db.Model, Entity, Dumpable):
    __tablename__ = 'user'

    whitelist = [
        'id',
        'created_on',
        'email_address',
    ]
    
    email_address = Column(String(200), unique=True, nullable=False)
    sessions = relationship('Session', back_populates='user', 
        cascade='save-update, merge, delete, delete-orphan')
    password_hash = Column(String(200), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def has_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, email_address, password, first_name):
        self.email_address = email_address
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name

    def __repr__(self):
        return '<User {id}>'.format(id=self.id)
