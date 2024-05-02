#!/usr/bin/env python3
"""
This module contains the sum_list function.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats, input_list, and returns their sum as a float.

    :param input_list: List of floats.
    :return: Sum of the list as a float.
    """
    return sum(input_list)
