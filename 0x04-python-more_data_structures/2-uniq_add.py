#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ function that 
    adds all unique integers in a list
    """
    new_list = []
    sum = 0
    for element in my_list:
        if element not in my_list:
            sum = sum + element
            new_list.append(element)
    return sum
