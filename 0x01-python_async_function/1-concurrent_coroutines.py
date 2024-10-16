#!/usr/bin/env python3
"""
    Contains wait_n()
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments (in
    this order): n and max_delay. You will spawn wait_random n times with
    the specified max_delay.

    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because
    of concurrency.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # As each task completes, we add the result to the delays list
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
