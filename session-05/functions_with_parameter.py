# --------------------------------------------------------
#
# Void Function with Parameters Example
#
# Folder:    session-05
# Filename:  functions_with_parameter.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def welcome(name):
    print("-" * 50)
    print(f"Welcome to this demo, {name}")
    print("-" * 50)


# the welcome() function is a void (Non-fruitful) function
# it returns nothing, but it does display to output
# via the print function

welcome("")

welcome("Isaac")

welcome()  # ERROR! missing the argument
