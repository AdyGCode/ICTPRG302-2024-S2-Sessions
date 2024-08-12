# --------------------------------------------------------
#
# Demo of input and try with functions
#
# Creating an input function for decimal numbers
# that provides an error
#
# Folder:    session-05
# Filename:  demo_input_try_v2.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def get_decimal(prompt="Enter a number: "):
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
    # print("Total cost for " + str(quantity_apples) + "kg at $" +
    #       str(cost_of_apples) + " per kg is $" + str(total_cost))
    print(f"Total cost for {quantity_apples:<10.2f}kg "
          f"at ${cost_of_apples:>10.2f} per kg "
          f"is ${total_cost:^10.2f}")

