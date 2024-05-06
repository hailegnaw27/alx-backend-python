#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform

async def wait_random(max_delay: int) -> float:
    """
    Asynchronous function that waits for a random amount of time up to max_delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that creates an asyncio.Task for wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that calls wait_random n times.
    """
    return [await wait_random(max_delay) for _ in range(n)]

def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """
    Function that creates an asyncio.Task for wait_n function.
    """
    return asyncio.create_task(wait_n(n, max_delay))

# Example usage
async def test(max_delay: int) -> None:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

async def test_wait_n(n: int, max_delay: int) -> None:
    result = await wait_n(n, max_delay)
    print(result)

# Running the asyncio event loop
asyncio.run(test(5))  # Example for task_wait_random
asyncio.run(test_wait_n(5, 6))  # Example for task_wait_n

