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

    # bound method, it depends on the instance of the class in which the method is defined: self here
    def do_finalize(self):
        print('do_finalize')

    @staticmethod
    def static_do_finalize():
        print('static_do_finalize')

    # class method is not bound method, since it doesn't depend on the instance of the class
    @classmethod
    def class_do_finalize(cls):
        print('class_do_finalize')

obj = ExpensiveObject()
obj_id = id(obj)

# Using a bound method of a tracked object as the callable can also prevent an object from being finalized properly.
f = weakref.finalize(obj, obj.do_finalize)
# f = weakref.finalize(obj, obj.static_do_finalize)
# f = weakref.finalize(obj, ExpensiveObject.static_do_finalize)
# f = weakref.finalize(obj, obj.class_do_finalize)
# f = weakref.finalize(obj, ExpensiveObject.class_do_finalize)
f.atexit = False

# Because the callable given to finalize is a bound method of the instance obj,
# the finalize object holds a reference to obj, which cannot be deleted and garbage collected.
del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')
