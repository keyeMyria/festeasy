import datetime

from backend.models import User, Product, Festival, Cart
from backend.models import Category, BaseFestival
from backend.models import Supplier


def get_dummy_data():
    """
    Returns a list of dummy data.
    """
    test_user = User(
        email_address='test@festeasy.co.za',
        password='123',
        is_admin=True,
        first_name='TestName',
        cart=Cart()
        )
    now = datetime.datetime.now()
    users = [
        test_user,
    ]
    drinks = Category(name='Drinks')
    beer = Category(name='Beer')
    food = Category(name='Food')
    woolies = Supplier(name='Woolies')
    pp = Supplier(name='Pick n Pay')
    products = [
        Product(
            name='Castle Lite Beer',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description.',
            categories=[beer, drinks],
            suppliers=[woolies, pp],
            ),
        Product(
            name='Lays Small Pack',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description.',
            categories=[food],
            suppliers=[woolies],
            ),
        Product(
            name='Coke Can',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description.',
            categories=[drinks],
            suppliers=[pp],
            ),
        Product(
            name='Windhoek Beer',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description',
            categories=[drinks, beer],
            suppliers=[woolies, pp],
            ),
        Product(
            name='Text Chocolate',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description',
            categories=[food],
            suppliers=[woolies, pp],
            ),
        Product(
            name='KitKat Chocolate',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='a description.',
            categories=[food],
            suppliers=[woolies],
            ),
        Product(
            name='Jelly Beans',
            cost_rands=10,
            is_enabled=True,
            price_rands=10,
            description='A description.',
            categories=[food],
            suppliers=[woolies],
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
