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
# To limit the values to unique combinations rather than permutations, use combinations().
# As long as the members of the input are unique, the output will not include any repeated values.
show(combinations('abcd', r=2))

print('---- input has duplicate ---')
# Unlike with permutations, the r argument to combinations() is required.
show(combinations('abcc', r=2))
# ab ac ac
# bc bc
# cc
