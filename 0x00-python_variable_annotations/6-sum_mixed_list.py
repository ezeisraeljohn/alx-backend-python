#!/usr/bin/env python3
"""sum mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_list (List[int, float]): a list containing combo of float and
        int

    Returns:
        float: returns the sum of the list as float
    """
    return sum(mxd_lst)
