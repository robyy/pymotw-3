#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import functools


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('  called myfunc with:', (a, b))


def test_func(a, b, c=111111):
    print('  -----called test_func with:', (a, b, c))

def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return


show_details('myfunc', myfunc)
myfunc('a', 3)
print()


# the class partial, which can be used to “wrap” a callable object with default arguments. The resulting object is
# itself callable and can be treated as though it is the original function. It takes all of the same arguments as the
# original, and can be invoked with extra positional or named arguments as well

# Set a different default value for 'b', but require
# the caller to provide 'a'.
p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)
p1('passing a')
p1('override b', b=5)
print()

# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')

# TypeError: myfunc() got multiple values for argument 'b'
# functools.partial(myfunc, 'default a', b=99), once positional argue is set, can not be changed and it will not be
# considered as postional argument when when invoked as partial
# p2('jjjjbbb', b=11111)

# TypeError: myfunc() got multiple values for argument 'b'
p2('jjjjbbb')

# FINE
p2(b=11111)
print()

print('Insufficient arguments:')
# p1()


p3 = functools.partial(test_func, 'default a', 'default b')
show_details('~~~~partial with defaults p3', p3, True)
p3()
# -----called test_func with: ('default a', 'default b', 'a')
p3('a')
# TypeError: test_func() takes from 2 to 3 positional arguments but 4 were given
p3('a', 'b')
