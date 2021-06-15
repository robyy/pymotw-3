#!/usr/bin/env python3
"""Using zip()
"""

# end_pymotw_header

# zip() returns an iterator that combines the elements of several iterators into tuples.
from pprint import pprint

for i in zip([1, 2, 3], ['a', 'b', 'c', 'd']):
    print(i)

# print('------')
pprint(zip([1, 2, 3], ['a', 'b', 'c']))
