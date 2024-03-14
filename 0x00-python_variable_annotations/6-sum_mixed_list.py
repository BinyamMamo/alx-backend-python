#!/usr/bin/env python3
"""
Task 6 - sums contents of a mixed list of integers and floats
"""

from typing import List


def sum_list(mxd_lst: List[int | float]) -> float:
    """
     returns the sum of all items in the list
    """
    from functools import reduce
    return reduce(lambda x, y: x + y, mxd_lst)
