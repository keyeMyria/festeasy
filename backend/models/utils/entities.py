import datetime
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime

from backend import db


class Entity(object):
    id = Column(Integer, primary_key=True)
    created_on = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False,
    )
    last_updated_on = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
    )
