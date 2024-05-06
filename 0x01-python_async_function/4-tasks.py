#!/usr/bin/env python3
"""
Async function to run multiple tasks concurrently.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with max_delay.
    Returns the list of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    return sorted(results)

