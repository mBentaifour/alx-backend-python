#!/usr/bin/env python3
"""Run time for four parallel comprehensions
async comprehension using an async generator"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it"""
    start_time = time.time()

    loop = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*loop)

    end_time = time.time()

    return end_time - start_time
