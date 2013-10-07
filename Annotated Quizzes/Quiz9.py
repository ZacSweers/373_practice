#!/usr/bin/env python

"""
CS373: Quiz #9 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

[(2, 3), (3, 4), (4, 5)]
[3, 4, 5]
[5, 7, 9]
-9
"""

print zip([2, 3, 4], [3, 4, 5])
print map(lambda x : x + 1, [2, 3, 4])
print map(lambda x, y : x + y, [2, 3, 4], [3, 4, 5])
print reduce(lambda x, y : x - y, [2, 3, 4], 0)
