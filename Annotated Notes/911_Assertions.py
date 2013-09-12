#!/usr/bin/env python

# -----------------------------------------------------------------------------
# - Annotations by Henri Sweers
# - If you add any, be sure to add your name to this!
# -----------------------------------------------------------------------------

# -------------
# Assertions.py
# -------------

"""
Turn OFF assertions at run time with -O.
% python -O Assertions.py
"""

print "Assertions.py"

# -----------------------------------------------------------------------------
# - Computes the cycle length of a given number 'n' using the collatz algorithm
# -----------------------------------------------------------------------------
def cycle_length (n) :

    # Assert n is greater than 0, otherwise this will throw an exception.
    # This is called checking preconditions
    assert n > 0

    # Initialize a counter variable
    c = 0

    # In class we decided this should actually be initialized to 1, in case the
    #   given input 'n' is 1. The cycle length of 1 is 1.
    c = 1

    # While loop for calculating. Repeats infinitely until n < 1, but for
    #   collatz we're really doing this until n == 1
    while n > 1 :

        # If n is even, divide by 2
        if (n % 2) == 0 :
            n = (n / 2)

        # If n is odd, multiply by 3 and add one
        else :
            n = (3 * n) + 1

        # Increment and then the while loop will repeat
        c += 1

    # Remember lowest possible valid input is 1, which has a cycle length of 1
    assert c > 0

    # Return our count
    return c

# Confirm the method above computes the proper results for given inputs
assert cycle_length(1) == 1
assert cycle_length(5) == 6

print "Cycle length of 5 is",
print cycle_length(5)

print "Done."

# -----------------------------------------------------------------------------
# - EXTRA NOTES
# - Notice how the method above isn't inside of a class. In Python we can do
#   this, but java we can't. The closest thing we'd have would be creating a
#   static method inside of a class (since you can call static methods without
#   an instance of the class; i.e. SomeClass.someMethod())
# - Notice there's also no type declarations
# - This algorithm essentially keeps running until n equals some power of 2,
#       which it then crashes down into one (will divide by two forever)
# -----------------------------------------------------------------------------

"""
Assertions.py
Traceback (most recent call last):
  File "./Assertions.py", line 26, in <module>
    assert cycle_length(1) == 1
  File "./Assertions.py", line 21, in cycle_length
    assert c > 0
AssertionError
"""
