"""Acronyms"""

def abbreviate(words):
    """
    :param words: string
    :return: string
    """

    acronym = ''
    words_list = words.replace(' - ', ' ').replace('-', ' ').replace('_', '').split(' ')
    for word in words_list:
        acronym += str(word)[0].upper()
        print(acronym)

    return acronym