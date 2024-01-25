#!/usr/bin/python3


def best_score(a_dictionary):
    """function that returns a key
    with the biggest integer value
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        winner = ""
        for x in my_list:
            if a_dictionary[x] > score:
                score = a_dictionary[x]
                winner = x

        return winner
