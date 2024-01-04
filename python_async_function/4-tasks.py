#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    completed_task_lst = []

    for _ in range(n):
        completed_task_lst.append(await task_wait_random(max_delay))

    return sorted(completed_task_lst)
