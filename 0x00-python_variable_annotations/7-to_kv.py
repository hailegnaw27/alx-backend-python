#!/usr/bin/env python3
"""
This module contains the to_kv function.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string, k, and an int or float, v, and returns a tuple.

    The first element of the tuple is the string k.
    The second element is the square of the int or float v.

    :param k: String key.
    :param v: Value which is either an int or float.
    :return: A tuple containing the string k and the square of v as a float.
    """
    return k, float(v ** 2)
