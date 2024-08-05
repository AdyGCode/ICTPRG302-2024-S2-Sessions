# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-04
# Filename:  is_something_demo.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------


character = input("Enter a letter: ")

print("Is it a digit? ", character.isdigit())
print("Is it alpha? ", character.isalpha())
print("Is it uppercase? ", character.isupper())
print("Is it lowercase? ", character.islower())

if character.isupper():
    print("Upper case!")
elif character.islower():
    print('Lower case!')

