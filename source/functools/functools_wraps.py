#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import functools


def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    print()


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('  decorated:', (a, b))
        print('  ', end=' ')
        return f(a, b=b)
    return decorated


def myfunc(a, b=2):
    """myfunc() is not complicated"""
    print('  myfunc:', (a, b))
    return


# The raw function
show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)
print()

# Wrap explicitly
wrapped_myfunc = simple_decorator(myfunc)
# wrapped_myfunc:
#   object: <function myfunc at 0x1023820d0>
#   __name__: myfunc
#   __doc__ 'myfunc() is not complicated'
# when wrap explicitly(even with @functools.wraps(f)), not thru decorator, the
# function object reference, __name__, __doc__ still the
# original function's, the the wrapped_myfunc
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to wrapped', 4)
print()


# Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    """ docs for decorated_myfunc  """
    myfunc(a, b)
    return


# decorated_myfunc:
#   object: <function decorated_myfunc at 0x1023821f0>
#   __name__: decorated_myfunc
#   __doc__ ' docs for decorated_myfunc  '
# use decorator(with @functools.wraps(f)), the
# function object reference, __name__, __doc__ are now the
# the decorated_myfunc, not the original func
show_details('decorated_myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args to decorated', 4)
