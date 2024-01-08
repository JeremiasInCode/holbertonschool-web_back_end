#!/usr/bin/env python3
"""Task 0: Simple helper function"""


def index_range(page, page_size) -> tuple:
    """index_range() function"""
    return (page * page_size) - page_size, page * page_size
