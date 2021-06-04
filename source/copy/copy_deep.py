#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Deep copy example

"""

#end_pymotw_header
import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('a')
my_list = [a]
dup = copy.deepcopy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)  # element of dup list is a new/different object than a

# False, dup and my_list are 2 different objects even for shallow copy
print('      dup is my_list:', (dup is my_list))

# True, == compares list content, contents are same based on MyClass.__eq__()
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))

# True, based on MyClass.__eq__()
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))
