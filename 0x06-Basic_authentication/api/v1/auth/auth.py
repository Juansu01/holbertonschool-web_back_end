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

        new_path = False

        for path_ in path:
            if path_ != "" and path_ != "v1" and path_ != "api":
                for name in route_names:
                    if name.startswith(path_):
                        new_path = f"/api/v1/{name}"

        for _path in excluded_paths:

            if "*" in _path:
                route = _path.split("/")[3]
                route = route.replace("*", "")
                for name in route_names:
                    if name.startswith(route):
                        tmp_exlcluded_paths.append(f"/api/v1/{name}/")

        if new_path and tmp_exlcluded_paths:
            if new_path in tmp_exlcluded_paths:
                return False

            if new_path in excluded_paths:
                return False
        elif excluded_paths:
            if path in tmp_exlcluded_paths:
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
