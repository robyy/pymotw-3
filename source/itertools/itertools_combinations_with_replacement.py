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


print('Unique pairs:\n')
# In this output, each input item is paired with itself as well as all of the other members of the input sequence.
show(combinations_with_replacement('abcd', r=2))


print('---- input has duplicate -----')
show(combinations_with_replacement('abcc', r=2))
# aa ab ac ac
# bb bc bc
# cc cc cc  the last cc is the last c in the input with itself
