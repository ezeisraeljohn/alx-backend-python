#!/usr/bin/env python3
"""Returns a tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple

    Args:
        k (str): Takes a string
        v (int | float): takes an int or float

    Returns:
        tuple: Returns a tuple
    """
    return (k, v**2)
