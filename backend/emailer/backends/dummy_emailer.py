from . import BaseEmailer


class DummyEmailer(BaseEmailer):
    """
    Emailer which does nothing.
    """
    def send_email(to, from_name, from_address, subject, body):
        pass
