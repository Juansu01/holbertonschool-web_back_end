"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds user to the database and returns User Object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Takes in kwargs and tries to find user if
        the keys are in the table's columns.
        Returns the User object.
        """

        if not kwargs:
            raise InvalidRequestError

        columns = User.__table__columns.keys()

        user = self._session.query(User).filter_by(**kwargs).first()

        if user:
            return user

        raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Finds user by id and updates the user's attributes.
        Doesn't return.
        """

        user = self.find_user_by(id=user_id)

        for k in kwargs.keys():
            if hasattr(user, k):
                continue
            else:
                raise ValueError

        for k, v in kwargs.items():
            setattr(user, k, v)

        self._session.commit()
