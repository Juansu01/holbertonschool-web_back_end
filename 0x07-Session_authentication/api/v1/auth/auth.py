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

        tmp_exlcluded_paths = []

        for _path in excluded_paths:

            if "*" in _path:
                route = _path.split("/")[3]
                route = route.replace("*", "")
                for name in route_names:
                    if name.startswith(route):
                        tmp_exlcluded_paths.append(f"/api/v1/{name}/")

        if path[-1] != '/':
            path += '/'

        if path in tmp_exlcluded_paths:
            return False

        if path in excluded_paths:
            return False

        if "uas" in path:
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
