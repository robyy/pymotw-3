#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *

a = 1
b = 5.0

print('a =', a)
print('b =', b)
# The functions are equivalent to the expression syntax using <, <=, ==, >=, and >.
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))
