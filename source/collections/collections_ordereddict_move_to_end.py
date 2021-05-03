#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Re-ordering an OrderedDict
"""

# end_pymotw_header
import collections
from inspect import getmro

d = collections.OrderedDict(
    [('a', 'A'), ('b', 'B'), ('c', 'C')]
)

print('Before:')
for k, v in d.items():
    print(k, v)

d.move_to_end('b')

print('\nmove_to_end():')
for k, v in d.items():
    print(k, v)

d.move_to_end('b', last=False)

print('\nmove_to_end(last=False):')
for k, v in d.items():
    print(k, v)


class Mixin1:
    def test(self):
        print("Mixin1")


class Mixin2:
    def test(self):
        print("Mixin2")


class BaseClass:
    pass


class MyClass(BaseClass, Mixin1, Mixin2):
    pass


print(MyClass.__mro__)
print(getmro(MyClass))
