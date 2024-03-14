#!/usr/bin/env python3
"""
Task 8 - Creates a function that multiplies a float by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that takes a float and returns the product
    """
    def multiply(x: float) -> float:
        """
        multiplys a float with a multiplier
        """
        return x * multiplier

    return multiply
