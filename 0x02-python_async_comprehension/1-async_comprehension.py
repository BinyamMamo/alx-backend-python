#!/usr/bin/env python3
"""
Task 1 - Import async_generator from the previous task and then
"""
import asyncio
from typing import AsyncGenerator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    Return a list of numbers generated at regular interval.
    """
    async_generator = __import__('0-async_generator').async_generator
    async for i in async_generator():
        yield i
