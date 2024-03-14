#!/usr/bin/env python3
"""
Task 9 - Calculates the length of each element in the input list.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples where each tuple contains an element from lst
    and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
