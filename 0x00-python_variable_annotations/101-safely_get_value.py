#!/usr/bin/env python3
"""
Duck-typed annotations for safely_get_value function
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value for the given key if it exists, otherwise
    returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
