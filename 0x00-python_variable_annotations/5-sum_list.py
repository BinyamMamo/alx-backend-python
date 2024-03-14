#!/usr/bin/env python3
"""
Task 5 - sums contents of a list with floating typed values
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
     returns the sum of all items in the list
    """
    from functools import reduce
    return reduce(lambda x, y: x + y, input_list)
