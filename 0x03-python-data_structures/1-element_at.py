#!/usr/bin/python3
def element_at(my_list, idx):
    list_length = len(my_list)
    for i in range(list_length):
        if idx > 0:
                if idx == my_list[i]:
                    return my_list[idx]
