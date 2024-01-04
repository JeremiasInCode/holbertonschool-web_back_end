#!/usr/bin/env python3
"""coroutine"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """asynchronous coroutine that generates random float numbers"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
