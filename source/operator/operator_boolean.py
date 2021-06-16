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
b = 5

print('a =', a)
print('b =', b)
print()

# not_() includes a trailing underscore because not is a Python keyword.
# truth() applies the same logic used when testing an expression in an if statement or converting an expression to a
# bool.
# is_() implements the same check used by the is keyword, and is_not() does the same test and returns
# the opposite answer.
print('not_(a)     :', not_(a))
print('truth(a)    :', truth(a))
print('is_(a, b)   :', is_(a, b))
print('is_not(a, b):', is_not(a, b))
