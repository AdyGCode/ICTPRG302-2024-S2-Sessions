# --------------------------------------------------------
#
# ADD PROGRAM TITLE HERE
#
# ADD SUMMARY OF PROGRAM HERE
#
# Folder:    session-04
# Filename:  demo_input_try_v2.py
# Author:    YOURNAME <STUDENT_ID@tafe.wa.edu.au>
# Version:   0.0
# 
# --------------------------------------------------------


quantity_apples = input("Quantity of Apples (kg)? ")
try:
    quantity_apples = float(quantity_apples)
except:
    print("ERROR: Quantity must be a number.")
    quit()

cost_of_apples = input("Cost per kilogram? ")
try:
    cost_of_apples = float(cost_of_apples)
except:
    print("ERROR: Cost must be a number.")
    quit()

total = quantity_apples * cost_of_apples

if quantity_apples == 0:
    print("Sorry that you did not want any apples")
elif cost_of_apples == 0:
    print("Your apples are free!")
else:
    print("Total cost for " + str(quantity_apples) + "kg at " +
          str(cost_of_apples) + " per kg is " + str(total))
