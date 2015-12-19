from flask_restful import Resource

from backend.models import Category
from backend.api.v1.schemas import CategorySchema


category_schema = CategorySchema()


class CategoryCollection(Resource):
    def get(self):
        categories = Category.query.all()
        return category_schema.dump(categories, many=True).data
