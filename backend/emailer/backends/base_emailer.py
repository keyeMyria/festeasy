class BaseEmailer(object):
    """
    Emailer from which all other Emailers inherit from.
    """
    def send_email(self, to, from_name, from_address, subject, body):
        raise NotImplementedError()
