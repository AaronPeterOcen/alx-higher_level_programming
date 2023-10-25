#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pint = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                pint += 1
    except IndexError:
        raise

    print()
    return pint
