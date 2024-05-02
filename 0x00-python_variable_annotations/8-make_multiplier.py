#!/usr/bin/env python3
"""
This module contains the make_multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies a float by multiplier.

    :param multiplier: The multiplier.
    :return: A function that takes a float and multiplies it by multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
