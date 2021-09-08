def square(number):
    """
    :param number: int - chessboard square number.
    :return: int - number of grains for a square number .  
    """
    if( 0 < number < 65 ):
        return 2 ** ( number - 1 )
    else:
        raise ValueError('Invalid chessboard square number.')


def total():
    """
    :return: int - total number of grains on the chessboard.  
    """
    total = 0
    for x in range(1, 65):
        total += square(x)
    return total