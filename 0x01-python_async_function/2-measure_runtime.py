#!/usr/bin/env python3
"""
    Contains measure_time()
"""
import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Return a float.
    """

    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time
    return total_time / n
