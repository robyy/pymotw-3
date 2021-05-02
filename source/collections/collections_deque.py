#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Double-ended queue.
"""

#end_pymotw_header
import collections

# def __init__(self, iterable=(), maxlen=None):
d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

print('------')
a = [10, 20, 30, 20]
a.remove(20)
print(a)
# a = [10, 30, 20]
# removed first instance of argument
