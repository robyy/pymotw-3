#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import gc
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
obj_id = id(obj)

# Giving the finalize instance a reference to the object it tracks(the third param - obj in below code) causes
# a reference to be retained, so the object is never garbage collected.
f = weakref.finalize(obj, on_finalize, obj)
# f = weakref.finalize(obj, on_finalize, 'bbbbb')
f.atexit = False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')
