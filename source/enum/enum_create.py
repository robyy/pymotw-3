#!/usr/bin/env python3
# encoding: utf-8
"""
"""

#end_pymotw_header
import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))
print(type(BugStatus.new))
print('-----------------')

class Parent:
    parent_class_var = 'parent_class_var'

p1 = Parent()
p2 = Parent()

p1.parent_class_var = 'instance p1'

print(Parent.parent_class_var)
print(p1.parent_class_var)
print(p2.parent_class_var)

# print(dir(Parent))
# print(dir(p1))
# print(dir(p2))

# print(dir(Parent.__dict__))
# print(dir(p1.__dict__))
# print(dir(p2.__dict__))

print('------------------')
for obj in (Parent, p1, p2):
    for att in dir(obj):
        print(att, getattr(obj, att))
    print('')

print(Parent.__class__.__mro__)
print(p1.__class__.__mro__)
print(p2.__class__.__mro__)
