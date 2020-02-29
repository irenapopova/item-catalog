# my notes about python basics syntax

# jupiter installed locally"

# Build-in function
dict(a=1)  # no
# i better directly create my dictionary
{"a": 1, 2: 5}

# instead of:
tuple(1, 2, 3)
(1, 2, 3)

# instead of:
list(1, 2, 3)
# do:
[1, 2, 3]
# len functions runs on  everythin (dict, tuple, list, sets, geneators)
len()

# tuples are the same thing as list in javascript

# open you will need
# you use it like so:

with open("filename") as variable:
    # variable is the file "filename"
    # variable can be any name
    pass

# f-strings
variable = 5
f"This is a string {variable} !"  # Prints "This is a string 5 !"
f = 10
# here above f is just a variable named f, and could be any name

# You don't need int and float
5 / 2  # = 2.5
# python automatically converts to float if need be

# The only use of type is for debugging
type(5)  # int


def very_useful_function():
    return


# This is run on execution BUT not on import
# This is only executed if called with python cheatsheet.py
# If someone does:
#import cheatsheet
# We don't want them to execute this code
if __name__ == 'main':
    # code code code
    very_useful_function()
    pass

# Because if we import cheatsheet.py in another file:
# import cheatsheet
# Then it will run every line one by one
# name is only defined if i do /run cheatsheet.py

# You won't need append on list/tuples/dictionnaries/etc and get and all that stuff:
# There's just two things you need for container modifications:

# comprehension
[i-1 for i in (1, 2, 3)]  # = [0,1,2]
# the second i takes the value and put it to the first i
# 1-1=0, 2-1=1, 2-1=2
# what is in parentheses is a tuple
# equivalent to:
[i-1 for i in [1, 2, 3]]  # list
[i-1 for i in {1: "a", 2: "whatever", 3: 2}]  # dictionary
[i-1 for i in [i+1 for i in [0, 1, 2]]]  # nested comprehension

# comprehensions works for anything
# you can create
[i-1 for i in (1, 2, 3)]  # list
{i-1 for i in (1, 2, 3)}  # set
{i-1: "a" for i in (1, 2, 3)]  # dictionnary
(i-1 for i in (1, 2, 3))  # generator

# generators are different but more advanced

# unpacking
a = [1, 2, 3]
b = [4, 5, 6]
[0, *a, 2, *b]  # output = [0, 1, 2, 3, 2, 4, 5, 6]
#! * is called splat, splat is just inside containers.

# this is different from multiplication because multiplication has two numbers or sides
1 * 2
a = 1
b = 2
a * b  # is also multiplication

# for dictionaries
a = {"a": 4, "b": 17}
b = {"a": 7, "c": 23}
# a and b are dictionaries
# = {"b": 17, "a": 7, "z": "whatever", "c": 23}
{"b": 5, **a, "z": "whatever", **b}
#! Two stars this time

# this is different from exponentiation because exponention also has two numbers or sides
1 ** 2
a = 1
b = 2
a ** b  # is also multiplication

# also, you can add lists:
[1, 2] + [3, 4]  # [1,2,3,4]

# you always want the d-versions
reversed([1, 2, 3])  # = [3,2,1
sorted([3, 4, 1, 0])  # = [0,1,3,4]

sort([1, 4, 3])  # = None

# The reason you don't want append, sort, etc is that they modify the list
a = [1, 3, 2]
b = sorted(a)

# a will be [1,3,2]
# b will be [1,2,3]

# That's what you want: To create the new object with the result without modifying the original

# you won't need id and hash, I may need them at one point some time

# get() is used very rarely

# quick rundowns of containers:
# all containers are traversable objects
[1, 2]  # list has square brackets
[1]  # single element list
(1, 2, 3)  # tuples have parentheses and comma
(1,)  # single tuple, singleton. #! comma is the tuple
{1: 2, 2: 3, }  # dictionaries have curly braces AND colons
{1: 2}  # single element dictionary
{1, 2}  # sets have just curly braces
{1}  # single element set
# only the tuple needs the comma when single

# STYLE: You can _always_ end with a comma (I recommend you do so)
[
    1,
    "string",
    46,
    5,
]  # if I have a lot of elements, I will put them one by one in line, and always end in a comma
# it is more consistent and easier to modify

d = {1: 2}
get(d)

# traversal
# for i in container is important:
for any_name_variable in [1, 2, 3]:  # a list is a traversable object
    do_stuff(any_name_variable)

# note that most of the time, you can just use list comprehension
# equivalent to:

[do_stuff() for i in [1, 2, 3]]
