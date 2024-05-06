#!/usr/bin/env python3
"""
Module containing the `task_wait_random` function.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps the `wait_random` coroutine.

    Parameters:
    max_delay (int): The maximum delay for `wait_random`.

    Returns:
    asyncio.Task: An asyncio task wrapping the `wait_random` coroutine.
    """
    # Create an asyncio Task that wraps the wait_random coroutine with max_delay
    return asyncio.create_task(wait_random(max_delay))

