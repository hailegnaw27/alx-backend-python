#!/usr/bin/env python3

import asyncio
import time
from typing import List
from 1-async_comprehension import async_comprehension  # Import async_comprehension from previous task

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()  # Record the start time

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Record the end time
    return end_time - start_time  # Return the total runtime in seconds

