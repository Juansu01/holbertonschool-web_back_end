#!/usr/bin/env python3
"""
This module defines the basic auth class.
"""

from base64 import encode
from api.v1.auth.auth import Auth
from base64 import b64decode


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
