#!/usr/bin/env python3
"""
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    from functools import reduce
    return reduce(lambda x, y: x + y, input_list)
