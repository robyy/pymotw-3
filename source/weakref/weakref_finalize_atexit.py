#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import sys
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
f = weakref.finalize(obj, on_finalize, 'extra argument')
# The finalize instance has a writable property atexit to control whether the callback is invoked as a program
# is exiting, if it hasn’t already been called.
# f.atexit = bool(int(sys.argv[1]))
# f.atexit = False
f.atexit = True
