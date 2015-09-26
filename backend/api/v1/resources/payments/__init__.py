from backend.api.v1 import v1_api
from .payments_singleton import PaymentSingleton


v1_api.add_resource(PaymentSingleton,
                    '/payments/<int:payment_id>')
