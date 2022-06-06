#!/usr/bin/env python3

"""
This module defines the make_multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a a multiplier function that multiplies
    using the multiplier float.
    """

    def function(num: float) -> float:
        "Multiplies num by multiplier float"
        return float(num * multiplier)

    return function
