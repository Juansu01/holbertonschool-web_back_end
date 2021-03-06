#!/usr/bin/env python3

"""This module defines the task_wait_n routine."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all delays in
    ascending order.
    """

    delays = []
    delays_asc = []

    for i in range(n):
        delays.append(task_wait_random(max_delay))

    for f in asyncio.as_completed(delays):
        res = await f
        delays_asc.append(res)

    return delays_asc
