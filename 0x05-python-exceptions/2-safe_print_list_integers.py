#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the elements of lists that are integers.

    Args:
        my_list: list to print the elements
        x: number of elements of my_list

    Returns:
        number of elements printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(mylist[i]), end="")
            ret += 1
        except(ValueError, TypeError):
            continue
    print("")
    return (ret)
