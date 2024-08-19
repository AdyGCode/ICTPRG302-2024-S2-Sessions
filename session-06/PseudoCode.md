# Session 06 - Pseudocode


## External 

The following video outlines pseudocode and how to write good pseudocode.

- [Kinsta: What Is Pseudocode? The Programmer's Time-Saving Tool](https://www.youtube.com/watch?v=zMRlK7mzows)

Also, you may want to read:

- [Demystifying Pseudocode: A Practical Guide with Test Examples](https://dev.to/angelotheman/from-logic-to-lines-unleashing-the-power-of-pseudocode-and-flow-charts-in-development-2615)


## What is Pseudocode

It is:

- natural language like
- does not compile/execute
- explains the steps to solve a problem
- has some level of detail

It isn't:

- a formal computer language

## Example

Here is part of the algorithm for making the batter for a cake:

```text
Put room-temperature butter and sugar into bowl
Repeat
    Combine (mix/beat) the butter and the sugar
Until light and fluffy

Add the eggs to the creamed butter
Repeat
    Mix eggs and creamed butter
Until combined

In a second bowl, add the liquid ingredients
Repeat
    Mix liquid ingredients
Until combined

Into another bowl, sift together the flour and other dry ingredients

Repeat
    Add a little dry ingredients to the butter-egg mix
    Mix together
    Add a little liquid ingredients to the butter-egg mixture
    Mix together
Until just enough to combine

```

## Pseudocode Building Blocks

There are a number of basic building blocks:
- Start
- Sequence
- Iteration
- Conditional
- End

### Start & End



### Sequence

A sequence is a set of steps that are completed, and may include each of those shown below, plus Iterations and Conditionals.

| Block Type | Examples                          |
| ---------- | --------------------------------- |
| input      | Read, Get, Ask For, Obtain, Input |
| output     | Print, Display, Output            |
| compute    | Calculate, Determine, Work Out    |
| initialise | Set, Init, Initialise             |
| add        | Increment, Inc, Add               |
| subtract   | Decrement, Dec, Subtract          |


### Iteration

| Block Type                       | Example                                                |
| -------------------------------- | ------------------------------------------------------ |
| For                              | For count from 1 to 100<br>    Sequence<br>End For     |
| While                            | While count less than 100<br>    sequence<br>End While |
| Repeat ... Until<br>Do ... While | Repeat<br>    Sequence<br>Until Condition              |



### Conditional

Conditionals are the "decisions" of the computing world. They use the IF to show when a choice is to be made.

There is a special conditional called the CASE, which we will also show.

| Block Type | Example                                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IF         | IF _condition_ THEN  <br>    sequence1  <br>ELSE  <br>    sequence2  <br>ENDIF                                                                                                             |
| CASE       | CASE _expression_ OF  <br>    condition 1: sequence 1  <br>    condition 2: sequence 2  <br>    ......  <br>    condition n: sequence n  <br>OTHERS:  <br>    default sequence<br>END CASE |
The **Others** of the Case **block** may be written as **Otherwise**, or even **Default**, or **Else** if you want.


## Using Pseudocode to Write an Algorithm

This algorithm plays a game where the computer tries to guess your secret number. The smallest and largest values are set to 1 and 100 respectively. All numbers are integers.

> I have added letters to show lines for reference when we test the algorithm.

```text
Start

A) Set smallest to 1
B) Set largest to 100

C) Ask the user to pick a secret number between 1 and 100

D) Repeat
E)     Set (computer's) guess to half way between smallest and largest number (round down if necessary).
F)     Ask the user if your guess is too large, too small or correct.
G) 	If they say your guess is too small:
H) 	    Smallest is now the guess plus one
I) 	If they say your guess is too large:
J) 	    largest is now the guess minus one
K) Until guessed correctly

End
```



We can test our algorithm by creating a table... this is known as a trace table.

It shows each step of the algorithm at work.

| Step(s)       | Secret | Smallest | Largest | Guess | Output      |
| ------------- | ------ | -------- | ------- | ----- | ----------- |
| A,B,C         | 33     | 1        | 100     |       |             |
| D, E, F, G, I |        |          |         | 50    | Too large   |
| J, K          |        |          | 49      |       |             |
| D, E, F, G    |        |          |         | 25    | Too small   |
| H, I, K       |        | 26       |         |       |             |
|               |        |          |         | 37    | Too large   |
|               |        |          | 37      |       |             |
|               |        |          |         | 31    | Too small   |
|               |        | 32       |         |       |             |
|               |        |          |         | 34    | Too large   |
|               |        |          | 34      |       |             |
|               |        |          |         | 33    | Guessed it! |

So in Python...

```python
# A) Set smallest to 1
smallest = 1
# B) Set largest to 100
largest = 100

# C) Ask the user to pick a secret number between 1 and 100
print("Think of a number between 1 and 100, inclusive")

# D) Repeat
while True:
	# E) Set (computer's) guess to half way between smallest and largest number (round down if necessary).
	guess = int((largest + smallest) / 2)
	# F) Ask the user if your guess is too large, too small or correct.
	response = input(f"Is {guess} too (L)arge, (S)small, or (C)orrect?")
	# G) If they say your guess is too small:
	if response.lower() == "s":
		# H) Smallest is now the guess plus one
		smallest = guess
	# I) If they say your guess is too large:
	if response.lower() == "l": 
		# J) largest is now the guess minus one
		largest = guess
	# K) Until guessed correctly
	if response.lower() == "c":
		break
```

This is not too hard to follow so we will remove the comments:

```python
smallest = 1
largest = 100

print("Think of a number between 1 and 100, inclusive")

while True:
	guess = int((largest + smallest) / 2)
	response = input(f"Is {guess} too (L)arge, (S)small, or (C)orrect?")

	if response.lower() == "s":
		smallest = guess
	
	if response.lower() == "l": 
		largest = guess
	
	if response.lower() == "c":
		break
```