from backend.api.v1 import v1_api
from .invoice_singleton import InvoiceSingleton


v1_api.add_resource(InvoiceSingleton,
                    '/invoices/<int:invoice_id>')
