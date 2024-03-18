#!/usr/bin/env python3
"""
Task 3 - Create a measure_time function with integers n
and max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n
"""
import asyncio
import time


def measure_time(n :int, max_delay: int) -> float:
    """
     Measure how long it takes to run a number of coroutines
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time: float = time.time()

    total_time: float = stop_time - start_time
    return total_time / 2.0
