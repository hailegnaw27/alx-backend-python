#!/usr/bin/env python3
"""
Async function to run multiple coroutines concurrently.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay.
    Returns the list of all delays in ascending order.
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, _ = await asyncio.wait(delays)
    results = [task.result() for task in completed]
    return sorted(results)

