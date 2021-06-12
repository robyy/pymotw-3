#!/usr/bin/env python3
# encoding: utf-8
"""Least-recently-used cache
"""

# end_pymotw_header
import functools


@functools.lru_cache(maxsize=2)
def expensive(a, b):
    print('called expensive({}, {})'.format(a, b))
    return a * b


def make_call(a, b):
    print('({}, {})'.format(a, b), end=' ')
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')


make_call(1, 2)

# An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__()
# method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which compare equal
# must have the same hash value.
#
# Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash
# value internally.
#
# Most of Python’s immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are
# not; immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable. Objects
# which are instances of user-defined classes are hashable by default. They all compare unequal (except with
# themselves), and their hash value is derived from their id().
try:
    make_call([1], 2)
except TypeError as err:
    print('ERROR: {}'.format(err))

try:
    make_call(1, {'2': 'two'})
except TypeError as err:
    print('ERROR: {}'.format(err))
