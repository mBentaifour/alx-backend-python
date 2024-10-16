#!/usr/bin/env python3
"""async comprehension use with async Generator"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers then return the 10 random numbers"""
    random_numbers = [_ async for _ in async_generator()]
    return random_numbers
