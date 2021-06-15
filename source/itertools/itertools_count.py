#!/usr/bin/env python3
"""Using count()
"""

#end_pymotw_header
from itertools import *

# The count() function returns an iterator that produces consecutive integers, indefinitely.
# The first number can be passed as an argument (the default is zero).
# There is no upper bound argument (see the built-in range() for more control over the result set).
for i in zip(count(1), ['a', 'b', 'c']):
    print(i)  # This example stops because the list argument is consumed.
