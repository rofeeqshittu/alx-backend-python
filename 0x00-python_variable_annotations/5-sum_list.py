#!/usr/bin/env python3
"""
    Contains sum_list function
"""


def sum_list(input_list: list[float]) -> float:
    """ A type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float. """
    total: float  = 0.0
    for item in input_list:
        total += item
    return total
