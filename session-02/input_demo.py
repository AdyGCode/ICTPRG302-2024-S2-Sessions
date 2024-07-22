#######################################################################
#
# Input Demo
#
# YOU CAN ADD A DESCRIPTION LATER
#
# File:      Source/Repos/ICTPRG302/Sessions/session-02/input_demo.py
# Author:    Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Version:   1.0
#
# Copyright: © Copyright 2024, Adrian Gould
#
#######################################################################

# Define Constants (all CAPS!)
WELCOME = "Hello!"

# Define Variables
name = ""

# Ask the user for their name
# then display a welcome message
name = input("What is your name? ")
second_name = input("What is the other person's name? ")
print(WELCOME + " " + name + " and " + second_name)
