"""
This module defines the function safe_first_element.
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element.
    """
    if lst:
        return lst[0]
    else:
        return None
