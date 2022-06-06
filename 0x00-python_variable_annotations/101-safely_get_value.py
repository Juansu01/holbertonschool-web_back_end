#!/usr/bin/env python3

"""
This module defines the function safely_get_value.
"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]
                     = None) -> Union[Any, T]:
    """
    Returns the key value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
