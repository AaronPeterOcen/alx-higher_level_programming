#!/usr/bin/python3
def no_c(my_string):
    ns = ""
    for ch in my_string:
        if ch not in "cC":
            ns += ch
        return ns
