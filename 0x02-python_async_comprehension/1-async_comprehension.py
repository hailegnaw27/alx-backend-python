#!/usr/bin/env python3

import asyncio
from typing import List
from 0-async_generator import async_generator  # Import async_generator from previous task

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]

