#!/usr/bin/env python3
"""
Task 11 - Zooms in on the elements of the input tuple
          by repeating each item 'factor' times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    returns a new tuple with zoomed-in elements.
    """
    zoomed_in: Tuple = tuple(item for item in lst for _ in range(factor))
    return zoomed_in
