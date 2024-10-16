#!/usr/bin/env python3
"""
    Contains task_wait_random()
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function (do not create an async function, use the regular function
    syntax to do this) task_wait_random that takes an integer max_delay and
    returns a asyncio.Task.
    """
    # Create & return a task
    return asyncio.create_task(wait_random(max_delay))
