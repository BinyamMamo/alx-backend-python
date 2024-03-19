#!/usr/bin/env python3
"""
Task 1 - Import async_generator from the previous task and then
"""
from typing import Generator


async def async_comprehension() -> \
        Generator[float, None, None]:  # type: ignore
    """
    Return a list of numbers generated at regular interval.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
