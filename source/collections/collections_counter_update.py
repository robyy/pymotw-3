#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Updating counts.
"""

#end_pymotw_header
import collections

c = collections.Counter()
print('Initial :', c)  # Initial : Counter()

c.update('abcdaab')
print('Sequence:', c)  # Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

c.update({'a': 1, 'd': 5})
print('Dict    :', c)  # Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})

c.update(d=1, a=1)
print('kwargs  :', c)  # kwargs  : Counter({'d': 7, 'a': 5, 'b': 2, 'c': 1})
