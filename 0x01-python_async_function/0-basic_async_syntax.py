#!/usr/bin/env python3

"""This module defines the wait_random coroutine."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in max_delay, gets a random float between
    0 and max_delay, awaits for that amount of time
    and returns it.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
