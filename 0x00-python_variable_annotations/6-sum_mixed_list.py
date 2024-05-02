#!/usr/bin/env python3
"""
This module contains the sum_mixed_list function.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats, mxd_lst, and returns their sum as a float.

    :param mxd_lst: List of integers and floats.
    :return: Sum of the list as a float.
    """
    return sum(mxd_lst)
