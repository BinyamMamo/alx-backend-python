#!/usr/bin/env python3
"""
Task 2 - Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""
import asyncio
import time


async def measure_runtime():
    """
     Measures the runtime of async_comprehension by running it 4 times.
    """
    async_comp = __import__('1-async_comprehension').async_comprehension

    start_time = time.time()
    await asyncio.gather(*([async_comp()] * 4))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time
