from backend.api.v1 import v1_api
from .set_transaction import SetTrasnaction


v1_api.add_resource(SetTrasnaction,
                    '/payu-transactions')
