#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print()

a = iadd(a, b)
print('a = iadd(a, b) =>', a)
print()

c = iconcat(c, d)
print('c = iconcat(c, d) =>', c)

print('--- immutable type ---')
e = 5
f = 6
iadd(e, f)
print(iadd(e, f))  # 11operator_attrgetter.py
print(e)  # 5, original e doesn't change
print(f)  # 6

# def iadd(a, b):
#     "Same as a += b."
#     a += b
#     return a

print('----- mutable -----')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(iconcat(l1, l2))
print(l1)
print(l2)

# There is no such thing as primitive vs non-primitive values in python. There is however a distinction between
# mutable and immutable objects in python. Immutable objects such as ints, strings, floats, tuples, and booleans have
# a fixed internal state (e.g. you can't add or remove elements from a tuple, or change the value of an int object),
# whereas mutable objects such as list, dicts, sets etc. can be changed (e.g. you can add key-value pairs to a dict
# or sort a list in place).
