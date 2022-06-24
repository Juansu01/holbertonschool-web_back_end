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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

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
