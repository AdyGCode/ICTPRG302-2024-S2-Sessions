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

def get_decimal(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
        except:
            print("ERROR: Value entered must be a number.")
        else:
            return value


quantity_apples = get_decimal("Quantity of Apples (kg)? ")
cost_of_apples = get_decimal("Cost per kilogram? $")

total_cost = quantity_apples * cost_of_apples

if quantity_apples == 0:
    print("Sorry that you did not want any apples")
elif cost_of_apples == 0:
    print("Your apples are free!")
else:
    print("Total cost for " + str(quantity_apples) + "kg at $" +
          str(cost_of_apples) + " per kg is $" + str(total_cost))
