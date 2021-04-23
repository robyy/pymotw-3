#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Arithmetic operations with Counters
"""

#end_pymotw_header
import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

# Each time a new Counter is produced through an operation, any items with zero or negative counts are discarded
print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)  # returned result based on c1

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)



print('--------')
# Counter instances support arithmetic and set operations for aggregating results. This example shows the standard operators for
# creating new Counter instances, but the in-place operators +=, -=, &=, and |= are also supported.
c1 += c2
print(c1)
