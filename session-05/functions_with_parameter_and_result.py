# --------------------------------------------------------
#
# Void Function with Parameters, and a result Example
#
# Folder:    session-05
# Filename:  functions_with_parameter_and_result.py
# Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Version:   1.0
# 
# --------------------------------------------------------

def cost(quantity=0.0, price=0.0):
    total_cost = quantity * price
    return total_cost


print(cost(3, 2.5))

weight = 3.5
price_per_kilo = 3.35

total = cost(weight, price_per_kilo)
print(f"Total: ${total:1.2f}")

total_for_apples = cost(price=5.56, quantity=9)
print(f"Total: ${total_for_apples:4.2f}")
