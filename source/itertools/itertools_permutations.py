#!/usr/bin/env python3
# encoding: utf-8

# end_pymotw_header
from itertools import *


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('All permutations:\n')
# The permutations() function produces items from the input iterable combined in the possible permutations of
# the given length. It defaults to producing the full set of all permutations.
show(permutations('abcd'))

print('\nPairs:\n')
# Use the r argument to limit the length and number of the individual permutations returned.
show(permutations('abcd', r=3))
