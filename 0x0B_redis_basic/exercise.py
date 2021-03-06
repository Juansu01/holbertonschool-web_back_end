#!/usr/bin/env python3
"""
Module for Redis basic project.
"""

import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times method has been called.
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Decorator wrapper.
        """

        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores history of inputs and
    outputs.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Decorator wrapper.
        """
        inp = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inp)

        outp = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", outp)

        return outp

    return wrapper


def replay(fn: Callable):
    """
    Displays the history of calls of a particular function.
    """

    red = redis.Redis()
    function_name = fn.__qualname__
    calls_number = red.get(function_name)

    try:
        calls_number = calls_number.decode("utf-8")
    except Exception:
        calls_number = 0

    print(f"{function_name} was called {calls_number} times:")

    inputs = red.lrange(function_name + ":inputs", 0, -1)
    outputs = red.lrange(function_name + ":outputs", 0, -1)

    for _input, _output in zip(inputs, outputs):

        try:
            _input = _input.decode("utf-8")
        except Exception:
            _input = ""

        try:
            _output = _output.decode("utf-8")
        except Exception:
            _output = ""

        print(f"{function_name}(*{_input}) -> {_output}")


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

    @call_history
    @count_calls
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
