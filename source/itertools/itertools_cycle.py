#!/usr/bin/env python3
"""Using cycle().
"""

#end_pymotw_header
from itertools import *

# The cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely.
# Because it has to remember the entire contents of the input iterator, it may consume quite a bit of memory
# if the iterator is long.
for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
