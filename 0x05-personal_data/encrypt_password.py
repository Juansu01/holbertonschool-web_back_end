#!/usr/bin/env python3
"""
Encrypting passwords module.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the pasword and returns a byte string.
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates the provided password and returns a boolean.
    """

    if bcrypt.checkpw(password.encoded(), hashed_password):
        return True
    else:
        return False
