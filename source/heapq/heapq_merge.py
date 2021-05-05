#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import heapq
import random

# list(sorted(itertools.chain(*data)))

# For larger data sets, above technique can use a considerable amount of memory. Instead of sorting the entire combined sequence,
# merge() uses a heap to generate a new sequence one item at a time, determining the next item using a fixed amount of memory.
# Because the implementation of merge() uses a heap, it consumes memory based on the number of sequences being merged,
# rather than the number of items in those sequences.
random.seed(2016)

data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for i, d in enumerate(data):
    print('{}: {}'.format(i, d))

print(data)
print('\nMerged:')
for i in heapq.merge(*data):
    print(i, end=' ')
print()

print(heapq.merge(*data))
print(list(heapq.merge(*data)))
