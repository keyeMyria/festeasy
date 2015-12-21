from factory import Factory, post_generation

from backend.models import Product


class ProductFactory(Factory):
    class Meta:
        model = Product

    name = 'Chicken'
    description = 'This is some chicken.'
    is_enabled = True
    cost_rands = 9.99

    @post_generation
    def product_prices(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product_price in extracted:
                self.product_prices.append(product_price)
