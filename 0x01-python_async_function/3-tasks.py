#!/usr/bin/env python3
"""
Function to create an asyncio task.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio Task that runs wait_random with max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

