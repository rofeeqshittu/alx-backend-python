#!/usr/bin/env python3
"""
    A coroutine that generates random numbers asynchronously.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, asynchronously waits for 1 second,
    then yields a random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
