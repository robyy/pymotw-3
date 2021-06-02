#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Demonstrate WeakValueDictionary.
"""

# end_pymotw_header
import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('    (Deleting {})'.format(self))


def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        # decref, without this line, then there is still one extra var: o references ExpensiveObject('three')
        del o

    print('  all_refs =', end=' ')
    pprint(all_refs)
    print('\n  Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
        # decref, without this line, then there is still one extra var: value references ExpensiveObject('three')
        del value

    # remove all references to the objects except the cache
    print('\n  Cleanup:')
    # now only cache[key](cache is either dict or WeakValueDictionary) has reference to ExpensiveObject(name)
    del all_refs
    # this will gc WeakValueDictionary - will cause invoke of __del__() of ExpensiveObject (will not gc dict)
    gc.collect()

    print('\n  After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
    print('  demo returning')
    # all objects created inside functions will be gc: 3 ExpensiveObject, one two three
    return


demo(dict)
print()

demo(weakref.WeakValueDictionary)

print('')
print('------------')


def test_del_in_fn():
    o = ExpensiveObject('bbbb')
    # del o; with or without return; all of them will cause o.__del__()
    # del o
    # return

    o.__del__()  # there will be 2 '    (Deleting ExpensiveObject(bbbb))' printed


test_del_in_fn()
