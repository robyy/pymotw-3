#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Updating counts.
"""

#end_pymotw_header
import collections

c = collections.Counter('abcdaab')

# Counter does not raise KeyError for unknown items. If a value has not been seen in the input (as with e in this example), its count is 0.
for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
