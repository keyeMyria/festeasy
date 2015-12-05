from flask_restful import Resource

from backend.models import Category
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import CategorySchema


class CategoryCollection(Resource):
    def get(self):
        categories = Category.query.all()
        return marshal_or_fail('dump', categories, CategorySchema(), many=True)
