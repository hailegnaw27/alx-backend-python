#!/usr/bin/env python3
"""
This module contains the element_length function.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable list, lst, and returns a list of tuples containing each element and its length.

    :param lst: The iterable list of sequences.
    :return: List of tuples, each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]
