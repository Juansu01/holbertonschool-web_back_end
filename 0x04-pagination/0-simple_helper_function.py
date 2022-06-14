#!/usr/bin/env python3
"""
Pagination Project.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple size containing a start index and end index.
    """

    start_idx = (page - 1) * page_size
    return (start_idx, page * page_size)
