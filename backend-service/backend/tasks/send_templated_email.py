from jinja2 import Environment, PackageLoader

from backend import emailer


env = Environment(loader=PackageLoader('backend.emailer', 'templates'))


def send_templated_email(to, subject, template_name, data, from_name=None,
                            from_address=None):
    template = env.get_template(template_name)
    if not from_name:
        from_name = 'FestEasy'
    if not from_address:
        from_address = 'info@festeasy.co.za'
    emailer.send_email(
        to,
        'FestEasy',
        'info@festeasy.co.za',
        subject,
        template.render(
            data,
        )
    )
