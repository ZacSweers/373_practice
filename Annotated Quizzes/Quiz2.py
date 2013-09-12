#!/usr/bin/env python

"""
CS373: Quiz #2 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What happened in the three statements below?
    (3 pts)

a. added file "Add.txt"
b. git add Add.txt
c. git commit -m "..."
"""

% git status
# On branch master
nothing to commit (working directory clean)

% <a. what happened here>

% git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#   Add.txt
nothing added to commit but untracked files present (use "git add" to track)

% <b. what happened here>

% git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   new file:   Add.txt
#

% <c. what happened here>

% git status
# On branch master
nothing to commit (working directory clean)

""" ----------------------------------------------------------------------
 2. What are the four elements of the Circle of Life?
    [XP: Ch.2, Pg. 16]
    (1 pt)

define, estimate, choose, build
"""
