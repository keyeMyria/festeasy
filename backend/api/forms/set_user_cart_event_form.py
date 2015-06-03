from wtforms import Form, IntegerField
from wtforms.validators import Required, Email


class SetUserCartEventForm(Form):
    """ Used to set a user cart event for a user.
    """
    event_id = IntegerField('event_id', [Required()])
    
