#!/usr/bin/env python3
"""The Mapping
"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(
    dct: Mapping, key: Any, default: Union[TypeVar, None] = None
) -> Union[Any, TypeVar]:
    """None

    Args:
        dct (Mapping): None
        key (Any): _description_
        default (Union[TypeVar, None], optional): Returns a TypeVar.
        Defaults to None.

    Returns:
        Union[Any, TypeVar]:Returns A value
    """
    if key in dct:
        return dct[key]
    else:
        return default
