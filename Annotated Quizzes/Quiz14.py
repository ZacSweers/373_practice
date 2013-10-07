#!/usr/bin/env python

"""
CS373: Quiz #14 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (2 pts)

0 1 2 3 4 else
0 1 2
"""

for v in range(5) :
    print v,
else :
    print "else"

for v in range(5) :
    print v,
    if v == 2 :
        break
else :
    print "else"

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (2 pts)

[8, 10]
"""

a = [2, 3, 4]
b = [5, 6, 7]
print [x + y for x in a if x % 2 for y in b if y % 2]
