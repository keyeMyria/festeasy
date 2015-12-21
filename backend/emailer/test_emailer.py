from . import Emailer


class DummyEmailer(Emailer):
    """
    Emailer which is to be used for tests.
    """
    def send_email(to, from_name, from_address, subject, body):
        pass
