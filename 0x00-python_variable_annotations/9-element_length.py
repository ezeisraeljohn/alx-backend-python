#!/usr/bin/env python3
"""Annotated a function
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a List of tuples in sequence

    Args:
        lst (Iterable[Sequence]): an Iterable

    Returns:
        List[Tuple[Sequence, int]]: The return statement
    """
    return [(i, len(i)) for i in lst]
