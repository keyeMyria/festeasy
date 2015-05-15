from wtforms import Form, StringField
from wtforms.validators import Required, Email


class SetCurrentCartEventForm(Form):
    """ Used to set a users current_cart_event.
    """
    event_id = StringField('event_id', [Required()])
