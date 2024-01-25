#!/usr/bin/python3


def weight_average(my_list=[]):
    """function that returns the weighted
    average of all integers tuple"""
    if not my_list:
        return 0

    num = 0
    div = 0

    for element in my_list:
        num = num + element[0] * element[1]
        div = div + element[1]

    return (num / div)
