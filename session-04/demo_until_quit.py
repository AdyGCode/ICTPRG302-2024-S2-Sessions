# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-04
# Filename:  demo_until_quit.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------


value = None
while value != "QUIT":
    print("Enter a number or 'QUIT' to finish.")
    value = input("Enter your value: ")
    value = value.upper()
    if value != "QUIT":
        try:
            value = float(value)
        except:
            print("ERROR: Value must be a number or 'QUIT'.")
        else:
            print(value)

print("Value:", value)