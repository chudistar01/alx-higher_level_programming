#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints x elememt of the list.

    Args:
        my_list: list to print the element
        x: number of elements of my_list
    Returns:
    """
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)
