# --------------------------------------------------------
#
# Void Function with Named Parameters Example
#
# Folder:    session-05
# Filename:  functions_with_named_parameter.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def welcome(person=""):
    print("-" * 50)
    print(f"Welcome to this demo, {person}")
    print("-" * 50)


welcome()

welcome("Janette")

welcome(person="Jill")
