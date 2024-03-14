#!/usr/bin/env python3
"""
Task 11 - Safely retrieves a value from a dictionary (mapping).
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value associated with the key or the default value.
    """
    return dct[key] if key in dct else default
