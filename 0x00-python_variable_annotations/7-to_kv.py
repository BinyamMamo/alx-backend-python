#!/usr/bin/env python3
"""
Task 7 - Creates a tuple with a string and a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of the string @k and the square of @v.
    """
    return k, v ** 2
