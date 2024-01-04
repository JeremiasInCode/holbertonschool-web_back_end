#!/usr/bin/env python3
""" Annotate the below function’s parameters """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list that contains a tuple """
    lst = []

    for i in lst:
        lst.append(i, len(i))
    return lst
