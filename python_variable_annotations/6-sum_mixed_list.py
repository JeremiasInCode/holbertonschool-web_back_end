#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes the data and returns their sum as float """
    return sum(mxd_lst)
