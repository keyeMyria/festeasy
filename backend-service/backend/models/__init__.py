from sqlalchemy_continuum import make_versioned
from backend import db


# TODO: Need to break up many-to-many relationships into
#       one-to-many many-to-one for continuum.
make_versioned()


from .sessions import Session
from .users import User
from .products import Product
from .festivals import Festival
from .order_products import OrderProduct
from .orders import Order
from .cart_products import CartProduct
from .carts import Cart
from .invoice_products import InvoiceProduct
from .payments import Payment
from .invoices import Invoice
from .categories import Category
from .product_categories import ProductCategory
from .suppliers import Supplier
from .stock_units import StockUnit
from .forgot_password_tokens import ForgotPasswordToken
from .packages import Package
from .packaged_stock_unit import PackagedStockUnit
from .collections import Collection
from .payu_transactions import PayUTransaction
from .images import Image
from .group import Group

db.configure_mappers()
