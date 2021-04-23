#!/usr/bin/env python3
# encoding: utf-8
"""
"""

#end_pymotw_header
import enum


class BugStatus(enum.Enum):

    new = (7, ['incomplete',
               'invalid',
               'wont_fix',
               'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ('new', 'fix_committed'))
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    # Enum member values are not restricted to integers. In fact, any type of object can be associated with a member.
    # If the value is a tuple like (3, ('new', 'fix_committed')), the members are passed as individual arguments to __init__().
    # so for in_progress = (3, ('new', 'fix_committed')): num is 3, transitions is ('new', 'fix_committed')
    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', BugStatus.in_progress.name)  # Name: in_progress
print('Name:', BugStatus.in_progress)  # Name: BugStatus.in_progress
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transitions, BugStatus.in_progress.num)  # Custom attribute: ('new', 'fix_committed') 3

# True, coz transitions here is ('new', 'fix_committed') defined in: in_progress = (3, ('new', 'fix_committed')), and
# BugStatus.new.name in self.transitions is True
print('Using attribute:',
      BugStatus.in_progress.can_transition(BugStatus.new))
