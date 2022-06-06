#!/usr/bin/env python3

"""
This module defines the element_length function.
"""

from typing import List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the length of each value.
    """
    return [(i, len(i)) for i in lst]
