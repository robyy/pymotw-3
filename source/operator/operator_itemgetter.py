#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *

l = [dict(val=-1 * i) for i in range(4)]
print('Dictionaries:')
print(' original:', l)

# Item getters work like lambda x,y=5: x[y]:
# Return a callable object that fetches the given item(s) from its operand.
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
g = itemgetter('val')

# g(i) equals i[val]
vals = [g(i) for i in l]
print('   values:', vals)
print('   sorted:', sorted(l, key=g))

print()
l = [(i, i * -2) for i in range(4)]
print('\nTuples:')
print(' original:', l)
g = itemgetter(1)

# Item getters work with mappings as well as sequences.
# g(i) equals i[1]
vals = [g(i) for i in l]
print('   values:', vals)
print('   sorted:', sorted(l, key=g))
