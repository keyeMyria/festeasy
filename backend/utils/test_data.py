import datetime

from backend.models import User, Product, Festival, Cart, Session
from backend.models import Category, BaseFestival, ProductPrice


def get_test_data():
    """
    Returns a list of test data.
    """
    test_user = User(
        email_address='test@festeasy.co.za',
        password='123',
        is_admin=True,
        first_name='TestName',
        cart=Cart()
        )
    now = datetime.datetime.now()
    never = now + datetime.timedelta(days=1000)
    session = Session(user=test_user, expires_on=never)
    session.generate_token()
    test_user.sessions.append(
        session,
    )
    users = [
        test_user,
    ]
    drinks = Category(name='Drinks')
    beer = Category(name='Beer')
    food = Category(name='Food')
    products = [
        Product(
            name='Castle Lite Beer',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description.',
            categories=[beer, drinks]
            ),
        Product(
            name='Lays Small Pack',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description.',
            categories=[food],
            ),
        Product(
            name='Coke Can',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description.',
            categories=[drinks],
            ),
        Product(
            name='Windhoek Beer',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description',
            categories=[drinks, beer],
            ),
        Product(
            name='Text Chocolate',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description',
            categories=[food],
            ),
        Product(
            name='KitKat Chocolate',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='a description.',
            categories=[food],
            ),
        Product(
            name='Jelly Beans',
            cost_rands=10,
            is_enabled=True,
            product_prices=[
                ProductPrice(amount_rands=10),
            ],
            description='A description.',
            categories=[food],
            ),
    ]
    rtd = BaseFestival(name='Rocking The Diasies')
    sun = BaseFestival(name='Sunflower Fest')
    oppi = BaseFestival(name='Oppie Koppie')
    festivals = [
        Festival(
            base_festival=rtd,
            name='Rocking The Daisies',
            starts_on=now + datetime.timedelta(days=2),
            ends_on=now + datetime.timedelta(days=4),
            description='This is a description.',
            website_link='http://rockingthedaisies.com/',
            ticket_link='http://seed.nutickets.co.za/RTD2016',
            facebook_link='https://www.facebook.com/rockingthedaisiesfestival/?fref=ts',
        ),
        Festival(
            base_festival=sun,
            name='Sunflower Fest',
            starts_on=now + datetime.timedelta(days=20),
            ends_on=now + datetime.timedelta(days=25),
            description='This is a another description.',
            website_link='http://www.capetownmagazine.com/events/sunflower-outdoor-music-festival/11_37_55771',
            ticket_link='http://www.capetownmagazine.com/events/sunflower-outdoor-music-festival/11_37_55771',
            facebook_link='https://www.facebook.com/SunflowerFest',
        ),
        Festival(
            base_festival=oppi,
            name='Oppie Koppie',
            starts_on=now + datetime.timedelta(days=27),
            ends_on=now + datetime.timedelta(days=30),
            description='This is a another description.',
            website_link='http://www.oppikoppi.co.za/',
            ticket_link='http://www.oppikoppi.co.za/',
            facebook_link='https://www.facebook.com/oppikoppifestival/',
            ),
    ]
    things = users + products + festivals
    return things
