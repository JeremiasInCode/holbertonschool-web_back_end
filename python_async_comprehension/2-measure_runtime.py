#!/usr/bin/env python3
"Task 2: Run time for four parallel comprehensions"
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """will execute async_comprehension four times
    in parallel using asyncio.gather"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    return time.perf_counter() - start
