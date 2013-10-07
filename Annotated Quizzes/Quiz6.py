#!/usr/bin/env python

"""
CS373: Quiz #6 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following program?
    (4 pts)

m1 f1 f2 m2 m4 m5 m6
m1 f1 m3 m5 m6
"""

def f (b) :
    print "f1",
    if b :
        raise Exception()
    print "f2",

try :
    print "m1",
    f(False)
    print "m2",
except Exception :
    print "m3",
else :
    print "m4",
finally :
    print "m5",
print "m6"

try :
    print "m1",
    f(True)
    print "m2",
except Exception :
    print "m3",
else :
    print "m4",
finally :
    print "m5",
print "m6"
