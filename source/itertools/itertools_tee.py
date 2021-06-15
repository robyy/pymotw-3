#!/usr/bin/env python3
"""Using tee()
"""

#end_pymotw_header
from itertools import *

# https://docs.python.org/3/library/itertools.html
# count()
#
# Arguments:
# start, [step]
#
# Results:
# start, start+step, start+2*step, …
#
# Example:
# count(10) --> 10 11 12 13 14 ...
r = islice(count(), 5)

# tee() has semantics similar to the Unix tee utility, which repeats the values it reads from its input
# and writes them to a named file and standard output. The iterators returned by tee() can be used to
# feed the same set of data into multiple algorithms to be processed in parallel.
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))


