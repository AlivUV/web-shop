from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Base, User, Client, Product, engine

Base.metadata.create_all()

with Session(engine) as session:
    admin = User(name='admin', email='admin@example.com', is_admin=True)
    admin.raw_password = 'pass'
    exp_bottle = Product(
        name='Exp bottle', 
        description='A bottle that contains experience.',
        stock=2,
        price=10.99
    )
    arrow = Product(
        name='Arrow', 
        description='Arrow.',
        stock=128,
        price=1.05
    )
    nautilus = Product(
        name='Nautilus', 
        description='A large shell that only can be found at the ocean.',
        stock=5,
        price=7.85
    )
    exp_bottle = Product(
        name='Brush', 
        description='A tool used in archaeology to excavate suspicious blocks.',
        stock=7,
        price=5.3
    )
    bow = Product(
        name='Bow', 
        description='A ranged weapon that shoots arrows.',
        stock=7,
        price=11.2
    )
    session.add_all([admin, exp_bottle])

    john_user = User(name='john', email='john@example.com')
    john_user.raw_password = 'pass'
    session.add(john_user)

    john_client = Client(user_id=session.scalar(select(User.id).order_by(User.id.desc())))
    session.add(john_client)

    test_user = User(name='test_user', email='test.user@example.com')
    test_user.raw_password = 'pass'
    session.add(test_user)
    test_client = Client(user_id=session.scalar(select(User.id).order_by(User.id.desc())))
    session.add(test_client)
    session.commit()
