#!/usr/bin/env python3
""" Async Comprehension task """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_gen...

    Returns:
    List[float]: A list containing 10 random floats.
    """
    return [num async for num in async_generator()]
