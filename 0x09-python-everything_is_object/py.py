#!/usr/bin/python3
"""
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
"""

a = (1, 2)
b = (1, 2)
a is b
