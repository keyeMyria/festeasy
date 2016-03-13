from factory import Factory

from backend.models import Supplier


class SupplierFactory(Factory):
    class Meta:
        model = Supplier

    name = 'Test Supplier'
    location = 'Cape Town'
    contact_numer = '021717177'
