#!/usr/bin/env python3
# encoding: utf-8
"""combine values
"""

# end_pymotw_header
from itertools import *


# accumulate() may be combined with any other function that takes two input values to achieve different results.
def f(a, b):
    print(a, b)
    return b + a + b


# functools.reduce returns a single result, itertools.accumulate returns a iterator which keeps
# all the temp result for every step.
print(list(accumulate('abcde', f)))
