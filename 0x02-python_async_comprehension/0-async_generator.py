#!/usr/bin/env python3

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates 10 random floating-point numbers.

    The function loops 10 times, asynchronously waits for 1 second
    between each iteration, and yields a random number between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator yielding random floats between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

