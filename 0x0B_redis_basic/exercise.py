#!/usr/bin/env python3
"""
Module for Redis basic project.
"""

import redis
from typing import Union
import uuid


class Cache():
    """
    Cache class for storing data.
    """

    def __init__(self):
        """
        Constructing method.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
