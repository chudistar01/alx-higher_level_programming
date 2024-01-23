#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    length = len(my_list)
    if idx < 0 or idx > length:
        for i in range(length):
            return copied_list
    else:
        copied_list[idx] = element
        return copied_list
