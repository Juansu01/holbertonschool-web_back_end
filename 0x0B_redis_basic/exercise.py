#!/usr/bin/env python3
"""
Module for Redis basic project.
"""

import redis
from typing import Union, Optional
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

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """
        Converts the data back to the desired format
        """
        value = self._redis.get(key)

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        Parameterizes value to str.
        """
        value = self._redis.get(key).decode("utf-8")
        return value

    def get_int(self, key: str) -> str:
        """
        Parameterizes value to int.
        """

        try:
            return int(self._redis.get(key).decode("utf-8"))
        except Exception:
            return 0
