#!/usr/bin/env python3
"task 1: Async comprehension"
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """this coroutine will collect 10 random numbers
    using an async comprehension over async_generator, then
    will return all those numbers."""
    list_of_yields = [i async for i in async_generator()]
    return list_of_yields
