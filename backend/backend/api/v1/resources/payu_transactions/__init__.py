from backend.api.v1 import v1_api
from .payu_transaction_collection import PayUTransactionCollection


v1_api.add_resource(PayUTransactionCollection,
                    '/payu-transactions')
