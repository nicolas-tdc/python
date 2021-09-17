"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sub'
SUPERLIST = 'super'
EQUAL = 'equal'
UNEQUAL = 'unequal'


def sublist(list_one, list_two):
    """
    :param list_one: list
    :param list_two: list
    :return: string - Sublist category
    """

    if list_one == list_two:
        return EQUAL
    elif (not list_one and list_two) or is_sub(list_one, list_two):
        return SUBLIST
    elif (list_one and not list_two) or is_sub(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sub(list_one, list_two):
    """
    :param list_one: list
    :param list_two: list
    :return: string - Sublist category
    """

    is_sublist = False

    if list_one[0] in list_two:
        superitems_indexes = [i for i, x in enumerate(list_two) if x == list_one[0]]

        for superitem_index in superitems_indexes:

            for index_one, item in enumerate(list_one):
                index_two = index_one + superitem_index

                if index_two < len(list_two):

                    if item == list_two[index_two]:
                        is_sublist = True
                    else:
                        is_sublist = False
                        break
                else:
                    is_sublist = False
                    break

            if is_sublist == True:
                break

    return is_sublist
