#!/usr/bin/env python3
"""
Module containing the measure_time function
"""

import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n
    """
    start_time = time.time()

    # Call wait_n to measure the execution time
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    # Calculate the total time and average time per execution
    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
