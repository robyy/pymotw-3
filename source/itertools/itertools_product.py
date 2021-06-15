#!/usr/bin/env python3
# encoding: utf-8

# end_pymotw_header
from itertools import *
import pprint

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

# Nested for loops that iterate over multiple sequences can often be replaced with product(),
# which produces a single iterable whose values are the Cartesian product of the set of input values.
DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

print(DECK)

for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        # if card[1] == 'S':
        print()
