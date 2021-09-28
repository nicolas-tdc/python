"""Prime factors"""
import math


def factors(value):
    """
    :param value: int
    :return: list - Prime factors of value
    """

    prime_factors = []

    while value % 2 == 0:
        value = update_list_and_value(value, 2, prime_factors)

    value_sqrt = int(math.sqrt(value)) + 1

    for odd in range(3, value_sqrt):
        while value % odd == 0:
            value = update_list_and_value(value, odd, prime_factors)

    if value != 1:
        prime_factors.append(value)

    return prime_factors


def update_list_and_value(value, divider, prime_factors):
    """
    :param value: int
    :param divider: int
    :param prime_factors: list
    :return: int
    """
    prime_factors.append(divider)
    value = value / divider

    return value
