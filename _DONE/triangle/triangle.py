"""Triangle"""
from itertools import chain

def equilateral(sides):
    """
    :param sides: list
    :return is_equilateral: boolean
    """
    is_triangle = triangle_is_valid(sides)
    sides_count = count_sides_recurrence(sides)
    is_equilateral = True if len(sides_count) == 1 and is_triangle else False

    return is_equilateral


def isosceles(sides):
    """
    :param sides: list
    :return is_isoceles: boolean
    """
    is_triangle = triangle_is_valid(sides)
    sides_count = count_sides_recurrence(sides)
    is_isoceles = True if (len(sides_count) == 2 or len(sides_count) == 1) and is_triangle else False

    return is_isoceles


def scalene(sides):
    """
    :param sides: list
    :return is_isoceles: boolean
    """
    is_triangle = triangle_is_valid(sides)
    sides_count = count_sides_recurrence(sides)
    is_scalene = True if len(sides_count) == 3 and is_triangle else False

    return is_scalene


def count_sides_recurrence(sides):
    """
    :param word: string
    :return: list - Count of each side recurrence in a triangle
    """

    sides_count = []

    for side in sides:

        if side not in chain(*sides_count):
            sides_count.append([side, sides.count(side)])

    return sides_count


def triangle_is_valid(sides):
    """
    :param sides: list
    :return: boolean
    """

    if any(side == 0 for side in sides):
        return False

    sides_total = sum(sides)
    for side in sides:
        if side >= sides_total - side:
            return False

    return True
