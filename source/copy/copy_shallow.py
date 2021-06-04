#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Shallow copy example

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
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
# False, When making a shallow copy of a list object, a NEW list is constructed and the elements of the
# original object are appended to it.
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))  # True, == compares content
# True, For a shallow copy, the MyClass instance is not duplicated, so the reference in the dup list is to the
# same object that is in my_list.
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))
