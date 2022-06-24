#!/usr/bin/env python3
"""
This module defines the auth class.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This is the Auth class that manages
    API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require auth, returns false.
        """

        return False

    def authorization_header(self, request=None) -> str:
        """
        This method returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method also returns None
        """
        return None
