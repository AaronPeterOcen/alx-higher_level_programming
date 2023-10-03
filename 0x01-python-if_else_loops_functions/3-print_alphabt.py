#!/usr/bin/python3
import string

res = ""

for letter in string.ascii_lowercase:
    if letter not in ['q', 'e']:
        res += letter
print(res)
