"""Colors"""

def colors():
    """
    :return: list - Color codes
    """

    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    """
    :param color: string
    :return: int - Color code
    """
    return colors().index(color)
