#!/usr/bin/env python

"""
CS373: Quiz #4 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (2 pts)

5 11
"""

def f (n) :
    return n + (n >> 1) + 1

print f(3),
print f(7)

""" ----------------------------------------------------------------------
 2. In the context of Project #1: Collatz, what is f() computing?
    (1 pt)

For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""

""" ----------------------------------------------------------------------
 3. Describe the three kinds of cache: lazy, eager, meta.
    (1 pt)

lazy: fill as you read
eager: fill before you read
meta: fill outside of program
"""
