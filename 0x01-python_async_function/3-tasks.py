#!/usr/bin/env python3
"""
Module containing the `measure_time` function.
"""

import asyncio
import time
from typing import Union
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for `wait_n(n, max_delay)`.

    Parameters:
    n (int): Number of times to spawn `wait_random`.
    max_delay (int): The maximum delay.

    Returns:
    float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

