#!/usr/bin/env python3
"""Using map()
"""


# end_pymotw_header

def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


print('Doubles:')
# The built-in map() function returns an ITERATOR that calls a function on the values in the input iterators,
# and returns the results. It stops when any input iterator is exhausted.
for i in map(times_two, range(5)):
    print(i)

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
# multiply returns a tuple: (x, y, x * y), *i, expand the tuple
# constructing a tuple from multiple iterators
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print('\nStopping:')
r1 = range(5)
r2 = range(2)
# It stops when any input iterator is exhausted.
for i in map(multiply, r1, r2):
    print(i)
