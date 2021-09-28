"""High Scores"""

def latest(scores):
    """
    :param scores: list
    :return: int
    """
    return scores[-1]

def personal_best(scores):
    """
    :param scores: list
    :return: int
    """
    return max(scores)


def personal_top_three(scores):
    """
    :param scores: list
    :return: list
    """
    return sorted(scores, reverse=True)[:3]
