#!/usr/bin/env python3
"""
This module defines the auth class.
"""
from flask import request
from typing import List, TypeVar
import re


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

        route_names = ["users", "status", "stats"]

        tmp_exlcluded_paths = []

        if path[-1] != '/':
            path += '/'

        for _path in excluded_paths:

            if len(_path) == 0:
                continue

            if "*" in _path:
                if path == _path:
                    return False
            else:
                if _path[:-1] == path[:len(_path) - 1]:
                    return False

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        This method returns None
        """
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method also returns None
        """
        return None
