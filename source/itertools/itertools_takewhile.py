#!/usr/bin/env python3
"""Using takewhile()
"""

#end_pymotw_header
from itertools import *


def should_take(x):
    print('Testing:', x)
    return x < 2


# The opposite of dropwhile() is takewhile(). It returns an iterator that itself returns
# items from the input iterator as long as the test function returns true.
for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)  # As soon as should_take() returns false, takewhile() stops processing the input.
    # Testing: -1
    # Yielding: -1
    # Testing: 0
    # Yielding: 0
    # Testing: 1
    # Yielding: 1
    # Testing: 2
