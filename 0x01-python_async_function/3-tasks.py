#!/usr/bin/env python3
"""
Task 3 - Write a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
     Create task for a function that delays by random amount.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
