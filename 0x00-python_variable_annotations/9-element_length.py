#!/usr/bin/env python3
"""
    Contains element_length function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return element Length """
    return [(i, len(i)) for i in lst]
