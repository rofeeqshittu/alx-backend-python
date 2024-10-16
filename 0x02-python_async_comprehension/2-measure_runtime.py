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
    await asyncio.gather(  # Run four async_comprehension tasks in parallel
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    end_time = time.perf_counter()
    return end_time - start_time  # Total time taken
