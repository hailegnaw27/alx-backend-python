#!/usr/bin/env python3
"""
This module contains the safe_first_element function.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence, lst, and returns the first element if it exists, otherwise None.

    :param lst: Sequence of any type.
    :return: First element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
