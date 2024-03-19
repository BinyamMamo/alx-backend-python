#!/usr/bin/env python3
"""
Task 0 - Write a coroutine called async_generator that takes no arguments.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
     Generate 10 numbers at regular intervals
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
