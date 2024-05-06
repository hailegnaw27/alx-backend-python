#!/usr/bin/env python3
"""
Module containing the wait_n coroutine
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time with async
    """
    delays = []

    # Create a list to store the tasks
    tasks = []

    # Create and add tasks to the list
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Wait for all tasks to complete
    for task in tasks:
        delay = await task
        delays.append(delay)

    # Sort the delays in ascending order
    delays.sort()

    return delays
