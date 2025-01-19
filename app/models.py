from datetime import datetime
from dotenv import load_dotenv
from os import environ

from flask_login import UserMixin
from sqlalchemy import Boolean, Date, Float, Integer, Sequence, String
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import Session
from typing import List
from werkzeug.security import generate_password_hash, check_password_hash


# Load environment variables from .env
load_dotenv()

engine = create_engine(f'{environ.get('DB_DBMS')}://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}/{environ.get('DB_NAME')}', echo=True)

class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    """
    Represents a user in the database.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        date_added (datetime): The date the user was added.
        is_active (bool): Whether the user is active.
        is_admin (bool): Whether the user is an administrator.
    """

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, Sequence('user_id_seq'), primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column(String(128))
    date_added: Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    client: Mapped['Client'] = relationship(
        'Client', back_populates='user', cascade='all, delete-orphan'
    )
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the User object.

        This method is used to provide a human-readable representation of the User object.
        It returns a string with the user's ID, name and email.
        
        Returns:
            str: A string representation of the User object.
        """
        return f'User(id={self.id}, name={self.name}, email={self.email})'
    
    def set_password(self, password):
        """
        Sets the user's password.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the provided password matches the user's password.
        """
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_id(id):
        """
        Retrieves a user by their ID.

        Args:
            id (int): The ID of the user to retrieve.

        Returns:
            User: The user with the specified ID, or None if not found.
        """
        with Session(engine) as session:
            user = select(User).where(User.id == id)
            return session.scalar(user)


class Client(Base):
    """
    Represents a client in the database.

    Attributes:
        client_id (int): Unique identifier for the client.
        user_id (int): The ID of the user associated with the client.
    """
    __tablename__ = 'clients'

    client_id: Mapped[int] = mapped_column(Integer, Sequence('client_id_seq'), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='client')
    orders: Mapped[List['Order']] = relationship(
        'Order', back_populates='client', cascade='all, delete-orphan'
    )
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Client object.

        This method is used to provide a human-readable representation of the Client object.
        It returns a string with the client's ID and user ID.

        Returns:
            str: A string representation of the Client object.
        """
        return f'Client(id={self.id!r}, user={self.user_id!r})'

    @staticmethod
    def get_by_id(id):
        """
        Retrieves a client by their ID.

        Args:
            id (int): The ID of the client to retrieve.

        Returns:
            Client: The client with the specified ID, or None if not found.
        """
        with Session(engine) as session:
            client = select(Client).where(Client.id == id)
            return session.scalar(client)


class Product(Base):
    """
    Represents a product in the database.

    Attributes:
        product_id (int): Unique identifier for the product.
        is_active (bool): Whether the product is active.
        name (str): The product's name.
        description (str): The product's description.
        stock (int): The product's stock level.
        price (float): The product's price.
    """
    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(Integer, Sequence('product_id_seq'), primary_key=True)
    is_active:Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    name: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(String(512))
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    offers_details: Mapped[List['Details']] = relationship(
        'Details', back_populates='product'
    )
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Product object.

        This method is used to provide a human-readable representation of the Product object.
        It returns a string with the product's ID and name.

        Returns:
            str: A string representation of the Product object.
        """
        return f'Product(id={self.product_id!r}, name={self.name!r})'



class Order(Base):
    """
    Represents an order in the database.

    Attributes:
        order_id (int): Unique identifier for the order.
        creation_date (datetime): The date the order was created.
        client_id (int): The ID of the client associated with the order.
    """
    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(Integer, Sequence('order_id_seq'), primary_key=True)
    creation_date: Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey('clients.client_id'))

    client: Mapped[Client] = relationship(back_populates='orders')
    order_details: Mapped[List['Details']] = relationship(
        'Details', back_populates='order', cascade='all, delete-orphan'
    )
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Order object.

        This method is used to provide a human-readable representation of the Order object.
        It returns a string with the order's ID, creation date, and client ID.

        Returns:
            dict: A dictionary representation of the Order object.
        """
        return f'Order(id={self.order_id!r}, creation={self.creation_date!r}, client={self.client_id!r})'


class Details(Base):
    """
    Represents the details of an order in the database.

    Attributes:
        detail_id (int): Unique identifier for the details.
        quantity (int): The quantity of the product ordered.
        price (float): The price of the product ordered.
        order_id (int): The ID of the order associated with the details.
        product_id (int): The ID of the product associated with the details.
    """
    __tablename__ = 'details'

    detail_id: Mapped[int] = mapped_column(Integer, Sequence('detail_id_seq'), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey('orders.order_id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.product_id'))

    product: Mapped[Product] = relationship(back_populates='offers_details')
    order: Mapped[Order] = relationship(back_populates='order_details')
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Details object.

        This method is used to provide a human-readable representation of the Details object.
        It returns a string with the detail's ID, order ID, product ID, quantity and price.

        Returns:
            str: A string representation of the Details object.
        """
        return f'Details(id={self.detail_id!r}, order={self.order_id!r}, product={self.product_id!r}, quantity={self.quantity!r}, price={self.price!r})'