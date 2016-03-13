from flask import Blueprint


bp = Blueprint('api', __name__)


@bp.route('/')
def hi():
    return 'API Here.'
