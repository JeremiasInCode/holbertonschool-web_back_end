#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    completed_task_lst = []

    for _ in range(n):
        completed_task_lst.append(await wait_random(max_delay))

    return sorted(completed_task_lst)
