### python my notes

#### Converting between Types

#### Comprehensions

#### List Comprehensions

List comprehensions are a unique way to create lists in Python. A list comprehension consists of brackets containing and expression followed by a for clause, then zero or more for or if clauses. The expressions can be any kind of Python object. List comprehensions will commonly take the form of [<value> for <vars> in <iter>].

A simple case: Say we want to turn a list of strings into a list of string lengths. We could do this with a for loop:

```python

>>> names = ["Nina", "Max", "Rose", "Jimmy"]
>>> my_list = [] # empty list
>>> for name in names:
...     my_list.append(len(name))
...
>>> print(my_list)
[4, 3, 4, 5]

```

much easier with a list comprehension:

```python

>>> names = ["Nina", "Max", "Rose", "Jimmy"]
>>> my_list = [len(name) for name in names]
>>> print(my_list)
[4, 3, 4, 5]
```

We can also use comprehensions to perform operations, and the lists we assemble can be composed of any type of Python object. For example:

```python
>>> names = ["Nina", "Max", "Rose", "Jimmy"]
>>> my_list = [("length", len(name) * 2) for name in names]
>>> print(my_list)
[('length', 8), ('length', 6), ('length', 8), ('length', 10)]
```

In the above example, we assemble a list of tuples - each tuple contains the element “length” as well as each number from the len() function multiplied by two.

#### Conditionals

I can also use conditionals (if statements) in my list comprehensions. For example, to quickly make a list of only the even lengths, you could do:

```python

>>> names = ["Nina", "Max", "Rose", "Jimmy"]
>>> my_list = [len(name) for name in names if len(name) % 2 == 0]
>>> print(my_list)
[4, 4]
```

Here, i check divide every string length by 2, and check to see if the remainder is 0 (using the modulo operator).

#### String Joining with a List Comprehension

the string.join() function. You can call this function on any string, pass it a list, and it will spit out a string with every element from the list “joined” by the string. For example, to get a comma-delimited list of numbers, you might be tempted to do:

```python
>>> my_string = ",".join([0, 1, 2, 3, 4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

```

ou can’t join a list of numbers without first converting them to strings. But you can do this easily with a list comprehension:

```python
>>> my_list = [0, 1, 2, 3, 4]
>>> my_string = ",".join([str(num) for num in my_list])
>>> print(my_string)
0,1,2,3,4

```

#### sum, min, max

Some mathematical functions, such as sum, min, and max, accept lists of numbers to operate on. For example, to get the sum of numbers between zero and five, you could do:

```python
my_sum = sum([0, 1, 2, 3, 4])
print(my_sum)
```

But remember, anywhere you can use a list, you can use a list comprehension. Say you want to get sum, minimum, and maximum of every number between 0 and 100 that is evenly divisible by 3? No sense typing out a whole list in advance, just use a comprehension:

```python
>>> my_sum = sum([num for num in range(0, 100) if num % 3 == 0])
>>> print(my_sum)
1683
>>> my_min = min([num for num in range(0, 100) if num % 3 == 0])
>>> print(my_min)
0
>>> my_max = max([num for num in range(0, 100) if num % 3 == 0])
>>> print(my_max)
99
```

#### List Operations

#### Slicing Lists

a[start:stop] # items start through stop-1
a[start:] # items start through the rest of the array
a[:stop] # items from the beginning through stop-1
a[:] # a copy of the whole array

There is also the step value, which can be used with any of the above

#### Sets nad Dictionaries

#### Generator Expressions

#### ZIP - Function

### tuple - has to be two items, one item is the key and the other is the value

https://docs.python.org/3/library/random.html

```python

import random
random.randint(0, 100)
```

The instance knows about the class.

#### Object Oriented Programming

#### Classes

#### Class Instance

#### Initializer Method

#### Class Methods

```python
@classmethod
```

### boolean is a subclass of int

#### Types, instances & issubclass

#### magic method : **sir** & **repr**

#### Inheritance

#### EXPRESSIONS

#### Exceptional types

#### Try expert

####
