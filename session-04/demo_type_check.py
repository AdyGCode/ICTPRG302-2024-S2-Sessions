# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-04
# Filename:  demo_type_check.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------

value = None

value_type = type(value)
if value_type == int:
    print("Integer")
elif value_type == float:
    print("Floating point")
elif value_type == str:
    print("String")
elif value_type == list:
    print("List")
elif value_type == dict:
    print("Dictionary")
elif value_type == tuple:
    print("Tuple")
else:
    print("Unknown type")