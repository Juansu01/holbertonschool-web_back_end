#!/usr/bin/env python3
"""
Module that defines authentication functions.
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    Returns a salted and hashed password.
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
