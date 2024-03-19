#!/usr/bin/env python3
"""
Task 0 - Write a coroutine called async_generator that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
     Generate 10 numbers at regular intervals
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
