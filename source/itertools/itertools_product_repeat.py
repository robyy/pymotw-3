#!/usr/bin/env python3
# encoding: utf-8

# end_pymotw_header
from itertools import *


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()


print('Repeat 2:\n')
# To compute the product of a sequence with itself, specify how many times the input should be repeated.
show(list(product(range(3), repeat=2)))

print('Repeat 3:\n')
show(list(product(range(3), repeat=3)))
