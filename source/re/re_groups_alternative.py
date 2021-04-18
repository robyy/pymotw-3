#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Matching alternative groups
"""

#end_pymotw_header
import re

from re_test_patterns_groups import test_patterns

# 'a((a|b)+)' (a then seq. of [ab])
#
# 'abbaabbba'
# 'abbaabbba'  ('bbaabbba', 'a')
#  the outer group is `bbaabbba`, then find (a|b) - the first inner group in it, so it matches single a or b, whichever is the LAST
#  character in the string. Only the last match is accessible
test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
     (r'a((a|b)+)', 'a then seq. of [ab]'),
     (r'a([ab]+)', 'a then seq. of [ab]'),],
)

print('------------------')


# the group is the last character matched in the pattern
test_patterns(
    'bcaabc',
    [(r'(a|b|c)+', 'seq. of [ab]'),
     (r'([abc])+', 'seq. of [ab]'),]
)

# https://docs.python.org/3/library/re.html
# If a group matches multiple times, only the last match is accessible:
m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
m.group(1)                        # Returns only the last match.
# 'c3'
