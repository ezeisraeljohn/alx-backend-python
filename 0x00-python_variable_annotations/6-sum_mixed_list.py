#!/usr/bin/env python3
"""sum mixed list
"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """_summary_

    Args:
        mxd_list (List[int, float]): a list containing combo of float and
        int

    Returns:
        float: returns the sum of the list as float
    """
    return sum(mxd_list)
