# --------------------------------------------------------
#
# Demo of Integer Input with error
#
# Folder:    session-05
# Filename:  demo_input_try_v3.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def get_integer(prompt="Enter a number: "):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except:
            print("ERROR: Value entered must be a number.")
        else:
            return value


chocolate_bars = get_integer("How many bars of chocolate? ")

if chocolate_bars == 0:
    print("Sorry that you did not want any apples")
else:
    for count in range(chocolate_bars):
        print("+" + "-" * 12 + "+")
        print("| chocolate! |")
        print("+" + "-" * 12 + "+")
        print()
