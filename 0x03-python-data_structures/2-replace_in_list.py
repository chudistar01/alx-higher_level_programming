#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_length = len(my_list)
    for i in range(list_length):
        if idx < 0:
            return(my_list)
        else:
            my_list[idx] = element
            return (my_list)
