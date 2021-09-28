"""Palindrome"""


def largest(min_factor, max_factor):
    """
    :param min_factor: int
    :param max_factor: int
    :return: tuple or not found string
    """
    if min_factor > max_factor:
        raise ValueError('Get back in line minimum factor')

    tuple = get_tuple(min_factor, max_factor, True)
    
    return tuple

def smallest(min_factor, max_factor):
    """
    :param min_factor: int
    :param max_factor: int
    :return: tuple
    """
    if min_factor > max_factor:
        raise ValueError('Get back in line minimum factor')

    tuple = get_tuple(min_factor, max_factor)
    return tuple

def get_tuple(min_factor, max_factor, reverse = False):
    
    """
    :param min_factor: int
    :param max_factor: int
    :return: tuple
    """
    palindromes = []
    factors_couples = []
    factors = list(range(min_factor, max_factor + 1))

    for first_factor in factors:
            for second_factor in factors:
                product = first_factor * second_factor

                if is_palindrome(product, reverse):
                    palindromes.append(product)

    if palindromes and reverse:
        palindrome = sorted(palindromes)[-1]
        factors_couples = get_factors_couples(palindrome, factors)
    elif palindromes and not reverse:
        palindrome = sorted(palindromes)[0]
        factors_couples = get_factors_couples(palindrome, factors)
    else:
        palindrome = None

    if palindrome and factors_couples:
        return (palindrome, factors_couples)
    else:
        return (None, [])

def is_palindrome(product, reverse = False):
    """
    :param product: int
    :return: boolean
    """
    is_palindrome = False
    product_length = len(str(product))

    if 0 <= product <= 9:
        is_palindrome = True
    elif product >= 10 and product_length % 2 == 0:
        is_palindrome = split_and_compare_product(str(product), product_length)
    elif product >= 10 and product_length % 2 != 0:
        middle = int(product_length / 2)
        str_product = str(product)
        product_even = str_product[:middle] + str_product[middle + 1:]
        product_length = product_length - 1
        is_palindrome = split_and_compare_product(product_even, product_length)

    return is_palindrome

def split_and_compare_product(product, product_length):
    """
    :param product: int
    :return: boolean
    """
    max_first = product_length / 2
    first = []
    second = []

    for i in range(0, product_length):
        if i < max_first:
            first.append(product[i])
        else:
            second.append(product[i])
            second.reverse()

    if first == second:
        is_palindrome = True
    else:
        is_palindrome = False

    return is_palindrome

def get_factors_couples(palindrome, factors):
    """
    :param palindrome: int
    :param factore: list
    :return: list
    """
    factors_couples = []
    for first_factor in factors:
        for second_factor in factors:
            if palindrome == first_factor * second_factor:
                factors_couples.append([first_factor, second_factor])

    return factors_couples
