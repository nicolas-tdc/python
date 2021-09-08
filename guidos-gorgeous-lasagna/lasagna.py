"""Lasagna module."""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Return remaining bake time.

    Calculate the estimated bake time remaining based on
    the parameters elapsed bake time and expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time.

    Calculate the total preparation time
    based on the parameter number of layers.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    Calculates the total elapsed time spent cooking the lasagna based
    on the parameters number of layers and elapsed bake time.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time
