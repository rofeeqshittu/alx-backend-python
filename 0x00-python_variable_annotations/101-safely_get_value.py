#!/usr/bin/env python3
"""
    Contains safely_get_value function
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T') # Represents the type of the value in the dictionary and the default
def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """ Safely get value """
    if key in dct:
        return dct[key]
    else:
        return default
