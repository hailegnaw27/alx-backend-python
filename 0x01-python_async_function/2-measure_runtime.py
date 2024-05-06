#!/usr/bin/env python3
"""
Module containing the `wait_n` coroutine.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns `wait_random` `n` times
    with the specified `max_delay` and returns a list of all delays.

    Parameters:
    n (int): Number of times to spawn `wait_random`.
    max_delay (int): The maximum delay.

    Returns:
    List[float]: List of all delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

