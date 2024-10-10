#!/usr/bin/env python3
"""
    Contains safely_get_value function
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T') # Represents the type of the value in the dictionary and the default
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ Retrieves a value from a dict using a given key. """
    if key in dct:
        return dct[key]
    else:
        return default
