#!/usr/bin/env python3
"""Using chain()
"""

#end_pymotw_header
from itertools import *

# The chain() function takes several iterators as arguments and returns a single iterator that produces the contents
# of all of the inputs as though they came from a single iterator.
# chain() makes it easy to process several sequences without constructing one large list.
for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()
