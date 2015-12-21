from factory import Factory

from backend.models import Category


class CategoryFactory(Factory):
    class Meta:
        model = Category

    name = 'A Category'
    description = 'A Category Description.'
