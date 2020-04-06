### slice notation

```python

 a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

```

```python
a[start:stop:step] # start through not past stop, by step
```

The key point to remember is that the _:stop_ value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

```

a step may be a negative number:

```python
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

Slice notation is used to extract a substring

l[start:end]

The slice() function returns a slice object that can use used to slice strings, lists, tuple etc.

The slice object is used to slice a given sequence (string, bytes, tuple, list or range) or any object which supports sequence protocol (implements **getitem**() and **len**() method).

The syntax of slice() is:

```python
slice(start, stop, step)
```

##### slice() Parameters

##### slice() can take three parameters:

start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.

Example 1: Create a slice object for slicing

```python
# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))


#output
slice(None, 3, None)
slice(1, 5, 2)

# result1 and result2 are slice objects.
```

Example 2: Get substring using slice object

```python
# Program to get a substring from the given string

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn

# output
Pyt
yhn
```

Example 3: Get substring using negative index

```python
py_string = 'Python'

# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object])   # noh

#output
noh
```

#### Everything in python is an instance, variables can be instance of a class

Slicing is an easy way to create sub-lists from larger lists. a slice can be used to obtain a subset of items from a list. A string is just a list of characters. For example:

```python
>>> my_string = "Hello, world!"
>>> my_string[7:12] # from 7 to 12
'world'

```

leave out one of the numbers in the slice. Leaving out the first number is equivalent to using a zero - think of this as “from the beginning.” Leaving out the last number is equivalent to using the length of the list you’re slicing - you can think of this as “until the end.” For example:

```python
>>> my_string = "Hello, world!"
>>> my_string[:5] # from zero to 5
'Hello'
>>> my_string[7:] # from 7 to the end
'world!'
```

#### to copy a list

leave out both sides of the slice - “from the beginning, until the end.”

```python

>>> my_new_string = my_string[:]
>>> my_new_string
'Hello, world!'
```

##### Negative Indexing

```python
>>> my_string = "Hello, world!"
>>> my_string[-6:] # from the end - 6 to the end
'world!'
>>> my_string[-10:-4] # from the end - 10 to the end - 4
'lo, wo'

```

##### Get sublist and sub-tuple using negative index

```python

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)
print(py_list[slice_object])  # ['n', 'o', 'h']

# contains indices -1 and -3
slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object]) # ('n', 'h')

# output

['n', 'o', 'h']
('n', 'h')

```

#### Slicing a List

To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify. To output the first three elements
in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.

```python
players = ['mari', 'martina', 'tom', 'irena', 'eli']
print(players[0:3])
```

any subset of a list can be generated. For example, if I want the second, third, and fourth items in a list, I would start the slice at index 1 and
end at index 4:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

#### Looping Through a Slice

a slice in a for loop can be used if I want to loop through a subset of
the elements in a list. In the next example we loop through the first three
players and print their names as part of a simple roster:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
u for player in players[:3]:
 print(player.title())

```

Instead of looping through the entire list of players , Python loops
through only the first three names:

```python
Here are the first three players on my team:
Charles
Martina
Michael

```

When working with data, slices can be used to process the data in chunks of a specific size.
