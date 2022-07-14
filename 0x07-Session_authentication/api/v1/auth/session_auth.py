#!/usr/bin/env python3
"""
This module defines the auth class.
"""
from flask import request
from typing import List, TypeVar
import re
import os
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    This is the Auth class that manages
    API authentication.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates session id if user exists.
        """

        if user_id is None:
            return None
        if type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns user id using session id.
        """

        if session_id is None:
            return None
        if type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)
