#!/usr/bin/env python3
"""Using tee()
"""

# end_pymotw_header
from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

# The new iterators created by tee() share their input, so the original iterator should not be used after
# the new ones are created.
print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

# The new iterators created by tee() share their input,
# so the original iterator should not be used after the new ones are created.
# If values are consumed from the original input, the new iterators will not produce those values.
print('i1:', list(i1))
print('i2:', list(i2))
