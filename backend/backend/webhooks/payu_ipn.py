from backend.webhooks import webhooks


@webhooks.route('/payu-ipn')
def payu_ipn():
    return 'payU IPN here.'
