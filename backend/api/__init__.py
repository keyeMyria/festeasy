from flask import Blueprint

from .v1 import v1_bp


bp = Blueprint('api', __name__)


@bp.route('/')
def hi():
    return 'API Here.'
