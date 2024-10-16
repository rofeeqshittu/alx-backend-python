#!/usr/bin/env python3
""" Measures runtime for running async comprehension in parallel """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    & measures the total runtime.

    Returns:
    float: The total runtime for executing the four comprehension
    """
    start_time = time.perf_counter()
    # Run/Unpack 4 async_comprehension tasks in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time  # Total time taken
