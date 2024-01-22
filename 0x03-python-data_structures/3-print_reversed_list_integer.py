#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    new_list = my_list[:]
    list_length = len(new_list)
    for i in range(list_length):
        print("{:}".format(new_list[i]))
