from flask import Blueprint
from flask_restful import Api


v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)


@v1_bp.route('/')
def hi():
    return 'V1 API Here.'
