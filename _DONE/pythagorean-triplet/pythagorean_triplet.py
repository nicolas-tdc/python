"""Pythagorean triplet"""
import math

def triplets_with_sum(number):
    """
    :param number: int
    :return: list
    """
    triplets = []

    for x in range (1, number):
        for y in range (x + 1, number):
            z = number - x - y
            if z*z == x*x + y*y:
                triplets.append([x, y, z])    

    return triplets
