"""Anagrams"""
from itertools import chain

def find_anagrams(word, candidates):
    """
    :param word: string
    :param candidates: list
    :return: list - List of anagrams
    """
    anagrams = []
    word_letters = word_to_letters_count(word)
    candidates = remove_duplicates_from_candidates(candidates)

    for candidate in candidates:
        candidate_letters = word_to_letters_count(candidate)

        if sorted(candidate_letters) == sorted(word_letters) and word.lower() != candidate.lower():
            anagrams.append(candidate)

    return anagrams

def word_to_letters_count(word):
    """
    :param word: string
    :return: list - Count of each letter occurences in a word
    """
    letters_count = []
    letters = list(word.lower())

    for letter in letters:

        if letter not in chain(*letters_count):
            letters_count.append([letter, letters.count(letter)])

    return letters_count

def remove_duplicates_from_candidates(candidates):
    """
    :param candidates: list
    :return: list - Candidates without duplicates
    """

    for candidate in candidates:
        temp = candidate.lower()
        candidates.remove(candidate)

        if any(temp != duplicate.lower() for duplicate in candidates):
            candidates.append(candidate)

    return candidates