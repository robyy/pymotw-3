#!/usr/bin/env python3
"""Using islice()
"""

# end_pymotw_header
from itertools import *

# The islice() function returns an iterator that returns selected items from the input iterator, by index.
print('Stop at 5:')
# islice() takes the same arguments as the slice operator for lists: start, stop, and step.
# The start and step arguments are optional.
for i in islice(range(100), 5):  # stop index not included
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):  # # stop index not included
    print(i, end=' ')
print('\n')
