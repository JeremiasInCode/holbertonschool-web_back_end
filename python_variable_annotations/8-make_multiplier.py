#!/usr/bin/env python3
"""type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create and return a multiplier function"""

    def multiplier_function(x: float) -> float:
        """multiply a value by the stored multiplier"""
        return x * multiplier

    return multiplier_function
