from flask_restful import Resource
from flask import current_app, request
from suds.client import Client
from suds.sax.element import Element
from suds.sax.attribute import Attribute

from backend import db
from backend.models import Invoice, PayUTransaction
from backend.api.utils import get_or_404
from backend.api.v1.schemas import PayUSetTransactionSchema
from backend.api.v1.schemas import PayUTransactionSchema


wsse = ('wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')


def payuMeaSetTransactionApiCall(args):
    username_token = Element('UsernameToken', ns=wsse)
    username = Element('Username', ns=wsse).setText(args['store']['soapUsername'])
    password = Element('Password', ns=wsse).setText(args['store']['soapPassword'])
    password.append(
        Attribute('Type', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText')
    )
    username_token_things = [
        username,
        password,
        Attribute('wsu:Id', 'UsernameToken-9'),
        Attribute('xmlns:wsu', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd'),
    ]
    for thing in username_token_things:
        username_token.append(thing)

    security = Element('Security', ns=wsse).addPrefix(p='SOAP-ENC', u='http://www.w3.org/2003/05/soap-encoding')
    security_things = [
        username_token,
        Attribute('SOAP-ENV:mustUnderstand', '1'),
        Attribute('xmlns:wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')
    ]
    for thing in security_things:
        security.append(thing)

    transaction = {
        'Api': 'ONE_ZERO',
        'Safekey': args['store']['safekey'],
        'TransactionType': 'PAYMENT',
        'AdditionalInformation': args['additional_info'],
        'Basket': args['basket'],
        'Customer': args['customer']
    }

    client = Client(
        current_app.config['PAYU_SET_TRANSACTION_URL'],
        faults=False,
    )
    client.set_options(soapheaders=[security])
    return client.service.setTransaction(**transaction)


class PayUTransactionCollection(Resource):
    def post(self):
        base_return_url = request.headers.get('Origin')
        invoice_id = request.get_json()['invoice_id']
        invoice = get_or_404(Invoice, Invoice.id == invoice_id)
        user = invoice.order.user
        store = {
            'soapUsername': current_app.config['PAYU_SOAP_USERNAME'],
            'soapPassword': current_app.config['PAYU_SOAP_PASSWORD'],
            'safekey': current_app.config['PAYU_SOAP_SAFE_KEY'],
        }
        basket = {
            'description': 'FestEasy Invoice #{0}'.format(invoice.id),
            'amountInCents': int(invoice.amount_due_rands * 100),
            'currencyCode': 'ZAR',
        }
        additional_info = {
            'merchantReference': invoice.id,
            'returnUrl': base_return_url + '/payment-confirmation',
            'cancelUrl': base_return_url + '/payment-cancellation',
            'supportedPaymentMethods': 'CREDITCARD,EFT_PRO',
            'notificationUrl': current_app.config['PAYU_NOTIFICATION_URL']
        }
        customer = {
            'merchantUserId': user.id,
            'email': user.email_address,
            'firstName': user.first_name,
        }

        result = payuMeaSetTransactionApiCall({
            'store': store,
            'basket': basket,
            'additional_info': additional_info,
            'customer': customer,
        })

        data = PayUSetTransactionSchema().dump(result[1]).data
        payu_transaction = PayUTransaction(**data)
        payu_transaction.invoice_id = invoice.id
        db.session.add(payu_transaction)
        db.session.commit()
        return PayUTransactionSchema().dump(payu_transaction).data
