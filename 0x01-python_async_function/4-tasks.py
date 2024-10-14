#!/usr/bin/env python3
"""task_wait_n function with asyncio"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of delays in ascending order"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay_list = []
    for future in asyncio.as_completed(tasks):
        result = await future
        delay_list.append(result)
    return delay_list
