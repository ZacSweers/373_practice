#!/usr/bin/env python

"""
CS373: Quiz #3 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. Show the cycle for 3.
    What is the cycle length?
    [Collatz]
    (2 pts)

3, 10, 5, 16, 8, 4, 2, 1
8
"""

""" ----------------------------------------------------------------------
 2. Which of the following is true? Maybe more than one.
    [Collatz]
    (1 pt)

a. (n / 2),  with n even, always produces an even
b. (n / 2),  with n even, always produces an odd
c. (3n + 1), with n odd,  always produces an even
d. (3n + 1), with n odd,  always produces an odd

c.
"""

""" ----------------------------------------------------------------------
 3. Given positive integers, b and e, let m = e / 2. If b < m, then
    max_cycle_length(b, e) = max_cycle_length(m, e). True or False?
    [Collatz]
    (1 pt)

True

Consider b = 10, e = 100.
Then m = 100 / 2 = 50.
max_cycle_length(10, 100) = max_cycle_length(50, 100)
All the numbers in the range [10, 49] can be mapped to numbers in the
range [50, 100] by one or more doublings, so none of the numbers in the
range [10, 49] could have a larger cycle length than the numbers in the
range [50, 100].
"""
