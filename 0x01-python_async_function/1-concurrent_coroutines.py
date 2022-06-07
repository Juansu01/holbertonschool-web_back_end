#!/usr/bin/env python3

"""This module defines the wait_n routine."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all delays in
    ascending order.
    """

    delays = []
    delays_asc = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    for f in asyncio.as_completed(delays):
        delays_asc.append(await f)

    return delays_asc
