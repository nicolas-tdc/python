"""Darts"""
import math

def score(x, y):
    """
    :param x: float
    :param y: float
    :return score: int
    Return the score for a dart position in a dartboard game 
    """
    center_distance = math.sqrt(x ** 2 + y ** 2)
    if center_distance <= 1:
        score = 10
    elif center_distance <= 5:
        score = 5
    elif center_distance <= 10:
        score = 1
    else:
        score = 0
    
    return score
