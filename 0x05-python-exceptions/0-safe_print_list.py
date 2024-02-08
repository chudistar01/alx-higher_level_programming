#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    """ prints x elememt of the list.

    Args:
        my_list: list to print the element
        x: number of elements of my_list
    Returns:
    """
    index = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            index += 1
        except IndexError:
            break
    print()
    return (index)
