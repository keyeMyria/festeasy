from backend.api.v1 import v1_api
from .category_collection import CategoryCollection

v1_api.add_resource(CategoryCollection,
                    '/categories')
