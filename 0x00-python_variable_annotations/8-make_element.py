#!/usr/bin/env python3
"""
    Contains make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Make multiplier function """
    def multiplier_function(value: float) -> float:
        """ Multiplier function """
        return value * multiplier
    return multiplier_function
