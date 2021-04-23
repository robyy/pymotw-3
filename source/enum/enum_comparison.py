#!/usr/bin/env python3
# encoding: utf-8
"""
"""

# end_pymotw_header
import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
      actual_state == desired_state,  # False
      actual_state == BugStatus.wont_fix)  # True
print('Identity:',
      actual_state is desired_state,  # False
      actual_state is BugStatus.wont_fix)  # True
print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))

print('')
print(id(BugStatus.wont_fix))
print(id(actual_state))
