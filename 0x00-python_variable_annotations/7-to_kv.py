#!/usr/bin/env python3

"""
This module defines the to_kv function.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple, the first element is k and the second
    element is the square of the int/float.
    """

    return (k, v**2)
