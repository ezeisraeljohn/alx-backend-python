#!/usr/bin/env python3
"""The functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function

    Args:
        multiplier (float): takes a float

    Returns:
        Callable[[float], float]: returns a function
    """

    return lambda n: n * multiplier
