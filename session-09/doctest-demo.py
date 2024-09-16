# --------------------------------------------------------
#
# DocBlock Demo for Python
#
# Demonstrate Doc Blocks in Python and show how to
# write DocTests
#
# Folder:    session-09
# Filename:  doctest-demo.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   0.0
# 
# ----------------------------------------------------------------------

import doctest


def add(first_number, second_number):
    """
    Add two numbers together

    Explain what the function does in detail

    :param first_number: int|float
    :param second_number: int|float
    :return: int|float

    >>> add(0,0)
    0

    >>> add(2,3)
    5

    >>> add(-2, -5)
    -7

    >>> add(1,1.5)
    2.5

    >>> add(2.5, -1)
    1.5

    >>> add(1.5,2.5)
    4.0
    """
    return first_number + second_number


doctest.testmod()

total = add(4, 6)
