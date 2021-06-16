#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *
from random import random


class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)


l = [MyObj(i) for i in range(5)]
print('objects   :', l)

# One of the most unusual features of the operator module is the concept of getters. These CALLABLE objects are
# constructed at RUNTIME and retrieve attributes of objects or contents from sequences. Getters are especially useful
# when working with iterators or generator sequences, as they incur less overhead than a lambda or Python function.

# Extract the 'arg' value from each object

# After f = attrgetter('name'), the call f(b) returns b.name.
#
# After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
#
# After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
g = attrgetter('arg')
vals = [g(i) for i in l]  # i is an MyObj object, g(i) returns MyObj(i).arg

# Attribute getters work like
# lambda x,n='attrname': getattr(x,n):
print('arg values:', vals)

# Sort using arg
# The list.reverse() method doesn't take any arguments.
l.reverse()  # in place reverse
print('reversed  :', l)

# key is an optional function, the result/return of invocation of key(data_item) will be used for sorting
# the key function will be implicitly invoked on every item of the iterable, here is l
# so g(l_item) = l_item.arg = MyObj(x).arg, so the sorting is based on my_obj.arg
print('sorted    :', sorted(l, key=g))


print('------ reverse test ------')
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)
