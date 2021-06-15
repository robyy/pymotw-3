#!/usr/bin/env python3
# encoding: utf-8
"""combine values
"""

# end_pymotw_header
from itertools import *

# The accumulate() function processes the input iterable, passing the nth and n+1st item to a function and
# producing the return value instead of either input. The default function used to combine the two values adds them,
# so accumulate() can be used to produce the cumulative sum of a series of numerical inputs.
print(list(accumulate(range(5))))

# When used with a sequence of non-integer values, the results depend on what it means to “add” two items together.
# The second example in this script shows that when accumulate() receives a string input, each response is a
# progressively longer prefix of that string.
print(list(accumulate('abcde')))
