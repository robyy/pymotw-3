#!/usr/bin/env python3
"""Using repeat()
"""

#end_pymotw_header
from itertools import *

# repeat() function returns an iterator that produces the same value each time it is accessed.
# The iterator returned by repeat() keeps returning data forever, unless the optional times argument is provided to
# limit it.
for i in repeat('over-and-over', 5):
    print(i)
