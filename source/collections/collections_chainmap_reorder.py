#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""Reading values from a ChainMap after reordering it
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

# The ChainMap stores the list of mappings over which it searches in a list in its maps attribute. This list is mutable,
# so it is possible to add new mappings directly or to change the order of the elements to control lookup and update behavior.
print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list
# The reversed() function returns the reversed ITERATOR of the given sequence. A sequence is an object that
# supports sequence protocols: __len__() and __getitem__() methods. For example, tuple, string, list, range, etc.
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

print('change maps')
m.maps.append({'e': 'EEEE'})
print(m)
print(m['e'])
