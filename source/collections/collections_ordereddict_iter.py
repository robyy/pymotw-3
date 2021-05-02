#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Iterating over an OrderedDict
"""

#end_pymotw_header
import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)

# In Python 3.7.0 the insertion-order preservation nature of dict objects has been declared to be an official part of
# the Python language spec. Therefore, you can depend on it.

# Python 3.6 (CPython)
# As of Python 3.6, for the CPython implementation of Python, dictionaries maintain insertion order by default. This is considered
# an implementation detail though; you should still use collections.OrderedDict if you want insertion ordering that's
# guaranteed across other implementations of Python.
