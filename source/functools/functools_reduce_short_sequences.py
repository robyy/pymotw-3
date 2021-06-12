#!/usr/bin/env python3
# encoding: utf-8
"""
"""

# end_pymotw_header
import functools


def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b


# Sequences with a single item automatically reduce to that value when no initializer is present.
print('Single item in sequence:',
      functools.reduce(do_reduce, [1]))

print('Single item in sequence with initializer:',
      functools.reduce(do_reduce, [1], 99))

# Empty lists generate an error, unless an initializer is provided.
print('Empty sequence with initializer:',
      functools.reduce(do_reduce, [], 99))

try:
    # Empty lists generate an error, unless an initializer is provided.
    print('Empty sequence:', functools.reduce(do_reduce, []))
# Because the initializer argument serves as a default, but is also combined with the new values if the
# input sequence is not empty, it is important to consider carefully whether its use is appropriate.
# When it does not make sense to combine the default with new values,
# it is better to catch the TypeError rather than passing an initializer.
except TypeError as err:
    print('ERROR: {}'.format(err))
