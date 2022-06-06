#!/usr/bin/env python3

"""
This module defines the sum_mixed_list function.
"""

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of the elements inside the list as a float.
    """

    return float(sum(input_list))
