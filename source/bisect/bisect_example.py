#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Exampe use of the bisect module.
"""
# end_pymotw_header
import bisect

# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in values:
    # bisect.bisect(a, x, lo=0, hi=len(a))
    # Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a instead of
    # before (to the left of) any existing entries of x in a.
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3}  {:3}'.format(i, position), l)

# This is a simple example. In fact, given the amount of data being manipulated, it might be faster to simply build the list and
# then sort it once. By contrast, for long lists, significant time and memory savings can be achieved using an
# insertion sort algorithm such as this, especially when the operation to compare two members of the list requires expensive computation.


# values needs to be already sorted, or the result in meaningless.
p = bisect.bisect(values, 33)
print(p)
bisect.insort(values, 33)
print(values)

print(all(val >= 1 for val in values))
