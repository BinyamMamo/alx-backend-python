#!/usr/bin/env python3
"""
Task 4 - Take the code from wait_n and alter it into
a new function task_wait_n
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
     Create a task that invokes a function to spawn a delay n times 
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    delays = await asyncio.create_task(wait_n(n, max_delay))
    return delays