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

def welcome(person="", character="-"):
    print(character * 50)
    print(f"Welcome to this demo, {person}")
    print(character * 50)


welcome()
welcome("Janette")
welcome("Josiah", "#")
# Cannot use welcome(person="Eve","%") as named parameters must be last
welcome("Stacey", character="*")
welcome(person="Bradley", character="=")
