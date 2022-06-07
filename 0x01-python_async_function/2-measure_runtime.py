#!/usr/bin/env python3

"""This module defines the measure_time routine."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time, and returns it
    as a float.
    """

    before = time.time()

    asyncio.run(wait_n(n, max_delay))

    after = time.time()

    return (after - before) / n
