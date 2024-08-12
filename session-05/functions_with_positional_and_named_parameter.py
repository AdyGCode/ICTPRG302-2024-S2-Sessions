# --------------------------------------------------------
#
# Function with Positional and Named Parameters
#
# Folder:    session-05
# Filename:  functions_with_positional_and_named_parameter.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def welcome(person, character="-"):
    print(character * 50)
    print(f"Welcome to this demo, {person:>10s}")
    print(character * 50)


welcome("Janette")
welcome("Jack", "=")
welcome("James", "")
welcome("Jill", character="*")
