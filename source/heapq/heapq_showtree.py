#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import math
from io import StringIO


# A heap is a tree-like data structure in which the child nodes have a sort-order relationship with the parents. Binary heaps can be
# represented using a list or array organized so that the children of element N are at positions 2*N+1 and 2*N+2 (for zero-based indexes).
# This layout makes it possible to rearrange heaps in place, so it is not necessary to reallocate as much memory when adding or removing
# items.
def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree. tree here is binary tree"""
    # The StringIO module an in-memory file-like object. This object can be used as input or output to the most function that
    # would expect a standard file object.
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))  # math.log(x[, base]), calculated as log(x)/log(base)
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        # if the tree is full binary tree, at current row, it will have the number of columns nodes.
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()
