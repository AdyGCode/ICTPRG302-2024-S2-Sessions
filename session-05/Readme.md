# Session 05: Functions, Strings and Lists


## Functions

Quick review notes on functions.
### Void (Non Fruitful) Functions

- Do not return a value

```python
def welcome():
    print("-" * 50)
    print("Welcome to this demo")
    print("-" * 50)


welcome()
```

Code: [functions_void.py](functions_void.py)


### Functions with (Positional) Parameters

- Define one or more parameters
- Accepts exactly the same number of arguments
- Each argument *must* match the parameter in the same position
- If number of arguments does not match number of parameters then an error will occur

```python
def welcome(persons_name):
    print("-" * 50)
    print(f"Welcome to this demo, {persons_name}")
    print("-" * 50)
```

Calling `welcome`, and missing the argument:

```python
welcome()
```

Gives output of:

```text
Traceback (most recent call last):
  File "C:\Users\5001775\Source\Repos\ICTPRG302\Sessions\session-05\functions_with_parameter.py", line 26, in <module>
    welcome()  # ERROR! missing the argument
    ^^^^^^^^^
TypeError: welcome() missing 1 required positional argument: 'persons_name'
```

> **Note:** 
> This tells us we are missing an argument for `persons_name`.
> It tells us that the error is most likely at line 26 of our code.

Code: [functions_with_parameter.py](functions_with_parameter.py)


### Functions with Named Parameters

- Naming parameters allows for default values
- Naming parameters allows for arguments to be reordered

```python
def welcome(person=""):
    print("-" * 50)
    print(f"Welcome to this demo, {person}")
    print("-" * 50)


welcome()
welcome("Janette")
welcome(person="Jill")
```

Code: [functions_with_named_parameter.py](functions_with_named_parameter.py)

### Functions with Named & Positional Parameters

- Naming parameters allows for default values
- Naming parameters allows for arguments to be reordered
- Named parameters **must** come **after** positional parameters

```python
def welcome(person, character="-"):
    # Welcome has positional (person) and named (character) parameters
    print(character * 50)
    print(f"Welcome to this demo, {person:>10s}")
    print(character * 50)


welcome("Janette")
welcome("Jack", "=")
welcome("James", "")
welcome("Jill", character="*") 
```

Code: [functions_with_positional_and_named_parameter.py](functions_with_positional_and_named_parameter.py)


Small change in this example - both parameters are named.

```python

def welcome(person="", character="-"):
    print(character * 50)
    print(f"Welcome to this demo, {person}")
    print(character * 50)


welcome()
welcome("Janette")
welcome("Josiah", "#")
# Cannot use welcome(person="Eve","%") as named parameters must be last
welcome("Stacey", character="*")
welcome(person="Bradley", character="=")
```

Code: [functions_with_multiple_named_parameters.py](functions_with_multiple_named_parameters.py)


### Functions that return results (Fruitful)

- usually have at least one parameter
- return (usually) one result


Example calculates the total cost of a product given the weight and the price per kilogram.

```python
def cost(quantity=0.0, price=0.0):
    total_cost = quantity * price
    return total_cost

weight = 3.5
price_per_kilo = 3.35

total = cost(weight, price_per_kilo)
print(f"Total: ${total:1.2f}")

total_for_apples = cost(price=5.56, quantity=9)
print(f"Total: ${total_for_apples:4.2f}")
```

Code: [functions_with_parameter_and_result.py](functions_with_parameter_and_result.py)

