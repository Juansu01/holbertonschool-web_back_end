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
        route_names = ["users", "status", "stats"]

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        slash_path = True if path[l_path - 1] == '/' else False
        for exc in excluded_paths:
            l_exc = len(exc)
            slash_exc = True if exc[l_exc - 1] == '/' else False

            if slash_path and not slash_exc:
                path = path[:-1]
            elif not slash_path and slash_exc:
                path += '/'

            if path == exc:
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
