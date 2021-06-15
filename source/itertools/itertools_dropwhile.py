#!/usr/bin/env python3
"""Using dropwhile()
"""

#end_pymotw_header
from itertools import *


def should_drop(x):
    print('Testing:', x)
    return x < 1


# The dropwhile() function returns an iterator that produces elements of the input iterator after a condition
# becomes false for the first time.
# dropwhile() does not filter every item of the input. After the condition is false the first time,
# all of the remaining items in the input are returned.
for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
    # Testing: -1
    # Testing: 0
    # Testing: 1
    # Yielding: 1
    # Yielding: 2
    # Yielding: -2
