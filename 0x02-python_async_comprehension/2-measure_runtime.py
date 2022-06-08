#!/usr/bin/env python3
"""
This module defines the measure_runtime coroutine.
"""

from asyncio import gather
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time in four parallel comprehensions.
    """

    start_count = time.time()
    await gather(*[async_comprehension() for _ in range(4)])
    stop_count = time.time()

    return stop_count - start_count
