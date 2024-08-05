# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    extras
# Filename:  except_too_broad.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------


value = input("Enter number:")
try:
    value = int(value)
except:
    # Bare except gives PyCharm hint
    # Adrian indicated that except ValueError
    # would be more 'precise'
    print("ERROR! Not a number")

