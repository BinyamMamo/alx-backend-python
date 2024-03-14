#!/usr/bin/env python3
"""
Task 10 - Check the first element of the input list.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input list if it exists,
    otherwise returns None.
    """
    return lst[0] if lst else None
