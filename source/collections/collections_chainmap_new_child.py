#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""ChainMap as a namespace stack
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)

# ChainMap provides a convenience method for creating a new instance with one extra mapping at the front of the maps list to
# make it easy to avoid modifying the existing underlying data structures.
m2 = m1.new_child()  # m2 is a new instance

print('m1 before:', m1)  # m1 before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
print('m2 before:', m2)  # m2 before: ChainMap({}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

m2['c'] = 'E'

# This stacking behavior is what makes it convenient to use ChainMap instances as template or application contexts. Specifically,
# it is easy to add or update values in one iteration, then discard the changes for the next iteration. We can see in below, m1 doesn't
# change, it's kinda a template or application contexts, when it's accessed in the future iteration, it remains the same
print('m1 after:', m1)  # m1 after: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
print('m2 after:', m2)  # m2 after: ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
print(m2['c'])
