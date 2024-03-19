#!/usr/bin/env python3
"""
Task 0 - Write a coroutine called async_generator that takes no arguments.
"""
import asyncio


async def async_generator():
    """
     Generate 10 numbers at regular intervals
    """
    import random

    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
