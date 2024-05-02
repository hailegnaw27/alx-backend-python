#!/usr/bin/env python3
"""
This module contains the zoom_array function.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> List[Any]:
    """
    Takes a tuple, lst, and an integer, factor (default is 2).

    Returns a list that contains each element of lst repeated factor times.

    :param lst: Tuple of any type.
    :param factor: Factor by which to zoom in on the array (default is 2).
    :return: A list with each element of lst repeated factor times.
    """
    zoomed_in: List[Any] = [item for item in lst for _ in range(factor)]
    return zoomed_in


# Example usage
if __name__ == "__main__":
    array: Tuple[int, ...] = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
    print(zoom_2x)
    print(zoom_3x)
