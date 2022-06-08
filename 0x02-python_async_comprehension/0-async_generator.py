#!/usr/bin/env python3
"""
This module defines the async_generator coroutine.
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Loops 10 times and yields a random number
    between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
