from .set_transaction import SetTrasnaction
from backend.api.v1 import v1_api


v1_api.add_resource(SetTrasnaction,
                    '/payu-transactions')
