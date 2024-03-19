#!/usr/bin/env python3
"""
Task 1 - Import async_generator from the previous task and then
write a coroutine called async_comprehension that takes no arguments.
"""
import asyncio


async def async_comprehension():
    """
     Return a list of numbers generated at regular interval.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
