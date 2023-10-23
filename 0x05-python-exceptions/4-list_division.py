#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    try:
        for i in range(list_length):
            try:
                nl.append(my_list_1[i] / my_list_2[i])
            except (IndexError, ZeroDivisionError, TypeError):
                print("division by 0 or wrong type")
                nl.append(0)
    except IndexError:
        print("out of range")
    finally:
        return nl
