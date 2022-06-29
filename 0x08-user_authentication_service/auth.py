#!/usr/bin/env python3
"""
Module that defines authentication functions.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> str:
    """
    Returns a salted and hashed password.
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Returns a brand new uuid
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        This method creates a new user and returns the User Object.
        """

        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")

        except NoResultFound:

            return self._db.add_user(email,
                                     _hash_password(password)
                                     )

    def valid_login(self, email: str, password: str) -> bool:
        """
        Finds user and validates the password.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        is_valid = bcrypt.checkpw(password.encode("UTF-8"),
                                  user.hashed_password)
        if is_valid:
            return True

        return False

    def create_session(self, email: str) -> str:
        """
        Finds user and updates the session ID.
        Returns id if user is found, otherwise it
        will return None.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        _id = _generate_uuid()

        self._db.update_user(user.id, session_id=_id)

        return _id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """
        Retrieves user from session id, returns the user object,
        None otherwise.
        """

        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None

            return user

        return None

    def destroy_session(self, user_id: int) -> None:
        """
        Updates the user's session if user is found.
        Returns None.
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None
