#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *

l = [dict(val=-1 * i) for i in range(4)]
print('Dictionaries:')
print(' original:', l)

# Item getters work like lambda x,y=5: x[y]:
# Return a callable object that fetches the given item(s) from its operand.
# After f = itemgetter(2), the call f(r) returns r[2].
# After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
g = itemgetter('val')

# g(i) equals i[val]
vals = [g(i) for i in l]
print('   values:', vals)
print('   sorted:', sorted(l, key=g))

print()
l = [(i, i * -2) for i in range(4)]
print('\nTuples:')
print(' original:', l)
g = itemgetter(1)

# Item getters work with mappings as well as sequences.
# g(i) equals i[1]
vals = [g(i) for i in l]
print('   values:', vals)
print('   sorted:', sorted(l, key=g))

print('----------')
lst = [(2, 3), (1, 4), (0, 5), (5, 0)]
lst.sort(key=itemgetter(0))
print(lst)

lst.sort(key=itemgetter(1))
print(lst)

print('---------')
# Two tuples can be compared by comparing their elements starting from first. If there is a tie (elements are equal),
# the second element is compared, and so on.
print((1, 3) > (1, 4))  # False
print((1, 36) > (1, 4))  # True
print((1, 2, 3) > (1, 2, 4))  # False
print((1, 4) < (2, 2))  # True
print((1, 4, 1) < (2, 1))  # True

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return error, age


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)

sorted_list = sorted(participant_list, key=lambda item: (100 - item[1], item[2]))
print(sorted_list)

print('-----')


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs


# This can be abstracted out into a wrapper function that can take a list and tuples of field and order to sort them
# on multiple passes.
print(student_objects)  # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(list(student_objects))  # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(multisort(list(student_objects), (('grade', True), ('age', False))))

# The reverse parameter still maintains sort stability (so that records with equal keys retain the original order).
# Interestingly, that effect can be simulated without the parameter by using the builtin reversed() function twice:
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
standard_way = sorted(data, key=itemgetter(0), reverse=True)
double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
assert standard_way == double_reversed
print(standard_way)
# [('red', 1), ('red', 2), ('blue', 1), ('blue', 2)]

print('')
print('--- The sort routines are guaranteed to use __lt__() when making comparisons between two objects ---')
# The sort routines are guaranteed to use __lt__() when making comparisons between two objects. So, it is easy to
# add a standard sort order to a class by defining an __lt__() method:
Student.__lt__ = lambda self, other: self.age < other.age
print(sorted(student_objects))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# Key functions need not depend directly on the objects being sorted. A key function can also access external resources.
# For instance, if the student grades are stored in a dictionary, they can be used to sort a separate list of student
# names:
students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
# what happens is: newgrades.__getitem__(single_student)
print(sorted(students, key=newgrades.__getitem__))
# ['jane', 'dave', 'john']
print(newgrades.__getitem__('john'))  # F
