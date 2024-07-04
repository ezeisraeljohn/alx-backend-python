#!/usr/bin/env python3
"""Annotate a doctype
"""

from typing import Sequence, Union, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return an element of a list
    Args:
        lst (Sequence[Any]): The list

    Returns:
        Union[Any, None]: Return any type
    """
    if lst:
        return lst[0]
    else:
        return None
