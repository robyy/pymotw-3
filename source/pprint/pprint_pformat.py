#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Formatting with pformat
"""

#end_pymotw_header
import logging
from pprint import pformat, pprint
from pprint_data import data

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
# To format a data structure without writing it directly to a stream (for example, for logging), use pformat()
# to build a string representation.
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())

for line in formatted.splitlines():
    print(line)

print('-------------')

for line in formatted.splitlines():
    pprint(line)
