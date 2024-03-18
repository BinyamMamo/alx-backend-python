#!/usr/bin/env python3
"""
Task 0 - Write an asynchronous coroutine that takes in an integer argument
"""
import asyncio

async def wait_random(max_delay:int=10) -> float:
    """
     Wait a random amount of time
    """
    import random
    delay:float = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
