#!/usr/bin/env python3
"""Using repeat() and map()
"""

#end_pymotw_header
from itertools import *

# The repeat() iterator does not need to be explicitly limited, since map() stops processing when any of
# its inputs ends, and the range() returns only five elements.
for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))

print('-----')
for j in starmap(lambda x, y: (x, y, x * y), [(1, 2), (3, 4)]):
    print('{:d} * {:d} = {:d}'.format(*j))
