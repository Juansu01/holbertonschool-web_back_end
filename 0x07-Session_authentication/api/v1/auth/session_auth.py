#!/usr/bin/env python3
"""
This module defines the auth class.
"""
from flask import request
from typing import List, TypeVar
import re
import os
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    This is the Auth class that manages
    API authentication.
    """
    pass
