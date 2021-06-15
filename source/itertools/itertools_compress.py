#!/usr/bin/env python3
"""Using filter()
"""

#end_pymotw_header
from itertools import *

every_third = cycle([False, False, True])
data = range(1, 10)

# compress() offers another way to filter the contents of an iterable. Instead of calling a function,
# it uses the values in another iterable to indicate when to accept a value and when to ignore it.
# The first argument is the data iterable to process. The second argument is a selector iterable that
# produces boolean values indicating which elements to
# take from the data input (a true value causes the value to be produced; a false value causes it to be ignored).
for i in compress(data, every_third):  # every_third will be reused until data is exhausted
    print(i, end=' ')
print()

print('---')
print((1, 2) == (1, 2))  # True
print((1, 2) is (1, 2))  # True
print((1, 2) is [1, 2])  # False
