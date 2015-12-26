class BaseEmailer(object):
    """
    Emailer from which all other Emailers inherit from.
    """
    def send_email(self, to, from_, subject, body):
        raise NotImplementedError()
