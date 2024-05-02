#!/usr/bin/env python3
"""
This module contains the safely_get_value function.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Takes a dictionary (Mapping), a key, and an optional default value.

    Returns the value corresponding to the key if the key exists in the dictionary, otherwise the default value.

    :param dct: A dictionary (Mapping).
    :param key: A key of any type.
    :param default: Optional default value.
    :return: Value corresponding to the key, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
