#!/usr/bin/env python3
"""
Task 1 - write an async routine called `wait_n` that takes in
2 int arguments (in this order): `n` and `max_delay`
"""

from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of all the delays (float values) in ascending order.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
