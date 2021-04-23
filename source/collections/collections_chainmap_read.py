#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""Reading values from a ChainMap
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

# The child mappings are searched in the order they are passed to the constructor, so the value reported for the key 'c'
# comes from the a dictionary.
m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))


print('----------------')
# # The child mappings are searched in the order they are passed to the constructor
m2 = collections.ChainMap(b, a)

# now the output is D, since b is passed to the constructor of ChainMap before a, the duplicate key mapping of 'c' in a dict is ignored.
print('c = {}'.format(m2['c']))
