#!/usr/bin/env python3
"""
This module defines the basic auth class.
"""

from base64 import encode
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BaiscAuth class that inherits from Auth.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts authorization header.
        """
        if authorization_header is None:
            return None

        if type(authorization_header) != str:
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header.split(' ', 1)[1]

        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Returns the decoded value of a Base64 string.
        """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            encoded = base64_authorization_header.encode("utf-8")
            return b64decode(encoded).decode("utf-8")
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Returns the user email and password from the
        Base64 decoded value.
        """

        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) != str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        split_credentials = decoded_base64_authorization_header.split(':')

        return (split_credentials[0], split_credentials[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email
        and password.
        """

        if type(user_email) != str or type(user_pwd) != str:
            return None

        try:
            users_with_email = User.search({"email": user_email})
        except Exception:
            return None

        for user in users_with_email:
            if user.is_valid_password(user_pwd):
                return user

        return None
