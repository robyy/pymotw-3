#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Produce the elements of the counter.
"""

#end_pymotw_header
import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)

# The elements() method returns an iterator that produces all of the items known to the Counter.
# The order of elements is not guaranteed, and items with counts less than or equal to zero are not included.
print(list(c.elements()))
