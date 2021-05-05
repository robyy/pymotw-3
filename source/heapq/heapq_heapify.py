#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random    :', data)

# If the data is already in memory, it is more efficient to use heapify() to rearrange the items of the list in place.
heapq.heapify(data)
print('heapified :')
show_tree(data)
