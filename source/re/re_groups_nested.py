#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Nested groups
"""

#end_pymotw_header
from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    # if nested groups, starting from most outer group, then inner groups left to right
    [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
)
