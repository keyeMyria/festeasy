import datetime

from backend.models import User, Product, Festival, Cart, Category, Supplier, \
    ProductCategory


def get_dummy_data():
    """Returns a list of dummy data.
    """
    items = []
    users = [User(
        email_address='test@festeasy.co.za',
        password='123',
        is_admin=True,
        first_name='TestName',
        cart=Cart()
    )]
    now = datetime.datetime.now()
    drinks = Category(name='Drinks')
    beer = Category(name='Beer')
    food = Category(name='Food')
    woolies = Supplier(name='Woolies')
    pp = Supplier(name='Pick n Pay')
    castle = Product(
        name='Castle Lite Beer',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description.',
    )
    castle.product_categories.extend([
        ProductCategory(product=castle, category=beer),
        ProductCategory(product=castle, category=drinks),
    ])
    items.append(castle)
    lays = Product(
        name='Lays Small Pack',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description.',
    )
    lays.product_categories.extend([
        ProductCategory(product=lays, category=food)
    ])
    items.append(lays)
    coke = Product(
        name='Coke Can',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description.',
    )
    coke.product_categories.extend([
        ProductCategory(product=coke, category=drinks)
    ])
    windhoek = Product(
        name='Windhoek Beer',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description',
    )
    windhoek.product_categories.extend([
        ProductCategory(product=windhoek, category=drinks),
        ProductCategory(product=windhoek, category=beer),
    ])
    items.append(windhoek)
    text = Product(
        name='Text Chocolate',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description',
    )
    text.product_categories.extend([
        ProductCategory(product=text, category=food),
    ])
    items.append(text)
    kitkat = Product(
        name='KitKat Chocolate',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='a description.',
    )
    kitkat.product_categories.extend([
        ProductCategory(product=kitkat, category=food),
    ])
    items.append(kitkat)
    jelly_beans = Product(
        name='Jelly Beans',
        cost_rands=10,
        is_enabled=True,
        price_rands=10,
        description='A description.',
    )
    jelly_beans.product_categories.extend([
        ProductCategory(product=jelly_beans, category=food),
    ])
    festivals = [
        Festival(
            name='Rocking The Daisies',
            starts_on=now + datetime.timedelta(days=2),
            ends_on=now + datetime.timedelta(days=4),
            description='This is a description.',
            website_link='http://rockingthedaisies.com/',
            ticket_link='http://seed.nutickets.co.za/RTD2016',
            facebook_link='https://www.facebook.com/rockingthedaisiesfestival/?fref=ts',
        ),
        Festival(
            name='Sunflower Fest',
            starts_on=now + datetime.timedelta(days=20),
            ends_on=now + datetime.timedelta(days=25),
            description='This is a another description.',
            website_link='http://www.capetownmagazine.com/events/sunflower-outdoor-music-festival/11_37_55771',
            ticket_link='http://www.capetownmagazine.com/events/sunflower-outdoor-music-festival/11_37_55771',
            facebook_link='https://www.facebook.com/SunflowerFest',
        ),
        Festival(
            name='Oppie Koppie',
            starts_on=now + datetime.timedelta(days=27),
            ends_on=now + datetime.timedelta(days=30),
            description='This is a another description.',
            website_link='http://www.oppikoppi.co.za/',
            ticket_link='http://www.oppikoppi.co.za/',
            facebook_link='https://www.facebook.com/oppikoppifestival/',
            ),
    ]
    items.extend(users)
    items.extend(festivals)
    return items
