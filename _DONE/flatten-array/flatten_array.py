"""Flatten array"""
from collections.abc import Iterable

def flatten(iterable):
    """
    :param iterable: list
    :return: list
    """
    flattened = []

    for i in iterable:
        if isinstance(i, Iterable):
            flattened = flattened + flatten(i)
        elif i != None:
            flattened.append(i)

    return flattened
