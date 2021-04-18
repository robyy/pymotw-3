#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Escaping escape codes
"""

#end_pymotw_header
from re_test_patterns import test_patterns

test_patterns(
    r'\d+ \D+ \s+',
    # escapes the backslash and plus characters, since both are meta-characters and have special meaning in a regular expression.
    # notice raw string here
    [(r'\\.\+', 'escape code')],
)
