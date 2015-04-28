import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime

from backend import db


class Dumpable(object):
    whitelist = []
    def dump(self):
        return {attr: getattr(self, attr) for attr in self.whitelist}


# All the models
from sessions import Session
from users import User
