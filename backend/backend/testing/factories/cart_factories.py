from factory import Factory

from backend.models import Cart


class CartFactory(Factory):
    class Meta:
        model = Cart
