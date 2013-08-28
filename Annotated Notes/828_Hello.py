#!/usr/bin/env python
# path to the python shell
# <-- pound sign is a one line comment

# -----------------------------------------------------------------------------
# - Annotations by Henri Sweers
# - If you add any, be sure to add your name to this!
# -----------------------------------------------------------------------------

# A block comment uses quotes and looks like this
"""
...some stuff...
"""

# --------
# Hello.py
# --------

# No comma after, prints with newline
print "Nothing to be done."
print "^^ see?"

# This would print the following:
"""
Nothing to be done.
^^ see?
"""

# With a comma, no new line
print "Nothing to be done...with no new line.",
print "<-- see?"

# This would print the following:
"""
Nothing to be done...with no new line. <-- see?
"""


"""
Implementation started in 1989 by Guido van Rossum of the Netherlands, now at Google.
--> He's actually left Google now to work at Dropbox, as of January 2013
Python is procedural, object-oriented, dynamically typed, and garbage collected.
"""

"""
# -----------------------------------------------------------------------------
# - the percent sign means it's run in the shell (from terminal, etc)
# - the -V argument prints the version of python
# -----------------------------------------------------------------------------
% python -V
Python 2.7.3
%

# -----------------------------------------------------------------------------
# - This runs our Hello.py
# - Remember python is an interpreter, so it runs the file as it reads it
# - As you can see, there's nothing to be done
# -----------------------------------------------------------------------------
% python Hello.py
Nothing to be done.
^^ see?
Nothing to be done...with no new line.  <-- see?
%

# -----------------------------------------------------------------------------
# - chmod changes file permissions
# - +x makes the file executable
# - u -> user, g -> group, o -> others
# - chmod a+x is the same as chmod ugo+x (a -> all)
# - This lets us execute the file directly (IF you specified the python
    path in line 1)
# -----------------------------------------------------------------------------
% chmod ugo+x Hello.py
% Hello.py
Nothing to be done.
^^ see?
Nothing to be done...with no new line.  <-- see?
%

# -----------------------------------------------------------------------------
# - Running python by itself enters into an interactive interpreter
# -----------------------------------------------------------------------------
% python
Python 2.7.3 (default, Aug  1 2012, 05:14:39)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

# -----------------------------------------------------------------------------
# - The ">>>" is kind of like the shell prompt within the interpreter
# - Here we're importing our Hello.py file (implicitly found the file despite
    not mentioning the extension, kind of like when you say "java something"
    even when you're actually referring to "something.class")
# -----------------------------------------------------------------------------
>>> import Hello
Nothing to be done.
^^ see?
Nothing to be done...with no new line.  <-- see?

# -----------------------------------------------------------------------------
# - This is how to exit the interpreter
# -----------------------------------------------------------------------------
>>> quit()
%



% python
Python 2.7.3 (default, Aug  1 2012, 05:14:39)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

# -----------------------------------------------------------------------------
# - How to ask for help!
# -----------------------------------------------------------------------------
>>> help()
Welcome to Python 2.6!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

# -----------------------------------------------------------------------------
# - "help>" is again kind of like the shell here
# - Here we look up info on the builtin "range" function
# -----------------------------------------------------------------------------
help> range
Help on built-in function range in module __builtin__:

range(...)
    range([start,] stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

# -----------------------------------------------------------------------------
# - How to quit the help shell
# -----------------------------------------------------------------------------
help> quit

>>> quit()
%



% python
Python 2.7.3 (default, Aug  1 2012, 05:14:39)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

# -----------------------------------------------------------------------------
# - Python is cute, so if you import this, you get a poem
# -----------------------------------------------------------------------------
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

>>> quit()
%
"""
