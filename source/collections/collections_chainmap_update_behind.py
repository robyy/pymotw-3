#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""Updating values underneath a ChainMap
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

# ChainMap kinda like SQL left join, keep all left, add incremental in the following
m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))

# A ChainMap does not cache the values in the child mappings. Thus, if their contents are modified, the results are reflected when
# the ChainMap is accessed.
a['c'] = 'E'
print('After : {}'.format(m['c']))  # After : E
b['c'] = 'BBBB'
print('After b changed: {}'.format(m['c']))  # After b changed: E
