# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-03
# Filename:  demo_for_characters.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

text = "2 Quick Foxes!"

for character in text:
    if character.islower():
        print(character, "is lower case")
    elif character.isdigit():
        print(character, "is a number")
    elif character.isupper():
        print(character, "is upper case")
    else:
        print(character, "is non alphanumeric")