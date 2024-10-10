#!/usr/bin/env python3
"""
    Contains safe_first_element function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ The type of the inputs are not known. """
    if lst:
        return lst[0]
    else:
        return None
