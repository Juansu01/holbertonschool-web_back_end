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
