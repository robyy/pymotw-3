#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import heapq
from heapq_heapdata import data

print('all       :', data)
print('3 largest :', heapq.nlargest(3, data))
# sorted(data) is [4, 9, 10, 11, 19], sorted(data)[-3:] is [10, 11, 19]. reversed returns a iterator
# steps: sort -> last n slice -> reverse -> make list
print('from sort :', list(reversed(sorted(data)[-3:])))
print('3 smallest:', heapq.nsmallest(3, data))
print('from sort :', sorted(data)[:3])
