from flask import Blueprint


api = Blueprint('v1', __name__)

from v1 import users
from v1 import sessions
from v1 import products
