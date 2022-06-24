#!/usr/bin/env python3
"""
This module defines the basic auth class.
"""

from api.v1.auth.auth import Auth


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
