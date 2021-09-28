"""Grades"""

def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    failed_students = 0
    for score in student_scores:
        if score <= 40:
            failed_students += 1

    return failed_students


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    above_students = []
    for score in student_scores:
        if score >= threshold:
            above_students.append(score)

    return above_students


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    thresholds = []
    interval = ( highest - 40 ) / 4
    for score in range(41, highest, round(interval)):
        thresholds.append(score)

    return thresholds


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    ranks = []
    for index, score in enumerate(student_scores):
        rank = index + 1
        ranks.append(f"{rank}. {student_names[index]}: {score}")

    return ranks

def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """

    for infos in student_info:
        if infos[1] == 100:
            return infos

    return "No perfect score."
