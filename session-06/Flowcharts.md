# Session 06 - Flowcharts




# Flowchart Symbols

> Note: Mermaid does not have all the symbols for traditional flowcharts, so you may need to 
> substitute to provide a meaningful experience.

### Start and End Points (Terminators)

```mermaid
---
title: Start and End Points
---
flowchart TD
    start_point([START])
    end_point([END])
```


### Connectors

Used to join up parts of a flowchart when the diagram cannot be placed on a single page, or 
would be too small if in a single line.

```mermaid
---
title: Connectors
---
flowchart TD
    start_point([start])-->connectorA((A))

    connectorB((A))-->end_point([end])
```

### Actions/Processes

Actions/Processes are any step that makes a change to data.

```mermaid
---
title: Actions/Processes
---
flowchart TD
    process_1(add quantity to total)
```


### Subroutine

When a sequence is too large to place into the main
diagram, we are able to separate it into a subroutine.

The subroutine is a rectangle with the ends having two lines.

When diagramming the subroutine, we simply create a new diagram
with a title that is the subroutine.

```mermaid
---
title: Subroutines
---
flowchart TD
    subroutine[[Calculate Fahrenheit]]
```

```mermaid
---
title: Calculate Fahrenheit
---
flowchart TD
    start_sub([Start])
    calc_f([Fahrenheit = 32 + Celcius * 9 / 5 ])
    end_sub([End])
    start_sub-->calc_f-->end_sub
```

### User/Manual Input

This is the main symbol that Mermaid does not
support, and we can replace with a standard
process or us a symbol like a chopped off triangle.


```mermaid
---
title: Input
---
flowchart TD
    input_1(Input Name)
    input_2[/Input Name\]
```

### Conditionals

Decisions in flowcharts are represented by the diamond.

```mermaid
---
title: Decisions/Conditionals
---
flowchart TD
    if_age{age > 21}
```

We combine this with yes and no branches...

```mermaid
---
title: Decisions/Conditionals
---
flowchart TD
    if_age{age > 21}
    if_age-->|Yes| open_account
    if_age-->|No| no_account
    open_account[[Open Account]]
    no_account[[Decline Account]]
    open_account-->end1
    no_account-->end1
    end1([End])
```

### Data Input/Output

Usually used to represent data to and from files or similar.

```mermaid
---
title: Input/Output
---
flowchart TD
    input_2[/Read names list/]
    output_2[/Write names list/]
```


## Guessing Game Flowchart

```mermaid
---
title: Guessing Game Flowchart
---
%%{ init: { 'flowchart': { 'curve': 'stepAfter' } } }%%
flowchart TD
    start([Start])
    smallest1(smallest = 1)
    largest1(largest = 1)
    secret[\User: Think of secret number/]
    guess1(guess = largest+smallest over 2)
    ask1[/ask if Larger, Smaller, Correct?\]
    if_smaller{guess is smaller?}
    smaller1(largest = guess)
    if_larger{guess is larger?}
    larger1(largest = guess)
    if_correct{guess is correct?}
    end1([End])

    start-->smallest1
    smallest1-->largest1
    largest1-->secret
    secret-->guess1
    guess1-->ask
    ask-->if_smaller
    if_smaller-->|Yes| smaller1
    if_smaller-->|No| if_larger
    smaller1-->if_larger
    if_larger-->|Yes| larger1
    larger1-->if_correct
    if_larger-->|No| if_correct
    if_correct-->|Yes| end1
    if_correct-->|No| guess1
    

```