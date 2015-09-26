from backend.api.v1 import v1_api
from .invoice_products_singleton import InvoiceProductSingleton


v1_api.add_resource(InvoiceProductSingleton,
                    '/invoice-products/<int:invoice_product_id>')
