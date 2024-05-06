import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time with async
    using task_wait_random
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays.sort()

    return delays
