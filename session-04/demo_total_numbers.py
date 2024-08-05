# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-04
# Filename:  demo_total_numbers.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

count = 0
total = 0
# initialise
number = 0
# test
while number >= 0:
    total = total + number
    # update
    number = int(input("Enter number: "))
    if number >= 0:
        count = count + 1

print("Total: ", total)
print("Count: ", count)
print("Mean: ", total / count)
