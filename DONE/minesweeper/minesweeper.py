"""Mine sweeper"""


def annotate(minefield):
    """
    :param minefield: list
    :return: list
    """
    error_handler(minefield)
    minefield_counts = []

    for line_index, line in enumerate(minefield):
        new_line = ''

        for char_index, char in enumerate(line):
            if char == ' ':
                char = 0
                max_index = len(line) - 1
                count_indexes = get_count_indexes(char_index, max_index)
                # Current line
                char += increment_square_value(line, count_indexes)
                # Previous line
                if line_index > 0:
                    previous_line = minefield[line_index-1]
                    char += increment_square_value(previous_line, count_indexes)
                # Next line
                if line_index < len(minefield) - 1:
                    next_line = minefield[line_index+1]
                    char += increment_square_value(next_line, count_indexes)

            char = ' ' if char == 0 else char
            new_line = new_line + str(char)

        minefield_counts.append(new_line)

    return minefield_counts


def get_count_indexes(char_index, max_index):
    """
    :param char_index: int
    :param max_index: int
    :return: list
    """
    count_indexes = []

    if char_index == 0 and max_index == 0:
        count_indexes = [char_index]
    elif char_index == 0:
        count_indexes = [char_index, char_index + 1]
    elif 0 < char_index < max_index:
        count_indexes = [char_index - 1, char_index, char_index + 1]
    elif char_index == max_index:
        count_indexes = [char_index - 1, char_index]

    return count_indexes


def increment_square_value(previous_line, count_indexes):
    """
    :param previous_line: string
    :param count_indexes: int
    :return: int
    """
    count = 0
    for index in count_indexes:
        if previous_line[index] == '*':
            count += 1

    return count
    

def error_handler(minefield):
    """
    :param minefield: list
    :return: void
    """
    for i, line in enumerate(minefield):
        for char in line:
            if char != ' ' and char != '*':
                raise ValueError('Invalid character.')
        if i > 0 and len(line) != length:
            raise ValueError('Lines not of same length.')
        length = len(line)
