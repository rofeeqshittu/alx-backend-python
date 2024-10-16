#!/usr/bin/env python3
"""
    Contains task_wait_n()
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.
    Return the list of all the delays (float values) in ascending order
    as they complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    # As each task completes, we append the result to the delays list
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
