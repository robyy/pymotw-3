#!/usr/bin/env python3
"""Grouping sequential values with groupby().
"""

# end_pymotw_header
import functools
from itertools import *
import operator
import pprint


@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


# Create a dataset of Point instances
data = list(map(Point,  # __init__ / constructor of class can be used
                cycle(islice(count(), 3)),  # (0, 1, 2, 0, 1, 2, 0), stop index not included
                islice(count(), 7)))  # (0, 1, 2, 3, 4, 5, 6)
print('Data:')
pprint.pprint(data, width=35)
print()

# Try to group the unsorted data based on X values
# The input sequence needs to be sorted on the key value so that the groupings will work out as expected.
print('Grouped, unsorted:')

# itertools.groupby(iterable, key=None)
# key is an optional function, the result/return of invocation of key(data_item) will be used for grouping/sorting
# the key function will be implicitly invoked on every item of the iterable
# After f = attrgetter('name'), the call f(b) returns b.name.
#
# After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
#
# After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Sort the data
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Group the sorted data based on X values
# The input sequence needs to be sorted on the key value so that the groupings will work out as expected.
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

print('-------- Grouped, sorted using customized key func -------:')


def data_key_func(data_item: Point):
    return data_item.x


for k, g in groupby(data, data_key_func):
    print(k, list(g))

    # 0 <itertools._grouper object at 0x104c6d0a0>
    # 1 <itertools._grouper object at 0x104c6d1f0>
    # 2 <itertools._grouper object at 0x104c6d0a0>
    # list([iterable]), so itertools._grouper is iterable/iterator
    print(k, g)
print()
