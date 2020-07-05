""" Description:

You are responsible for writing a program that will highlight the similarities
and differences between four different types of lists: a list of strings, a
list of integers, a list of floats, and a list of lists. For each list, your
program will describe the data type of the list, the elements of the list, and
the data type of the first element in the list. Your program will then
highlight the similarities and differences between sorting a list numerically
and alphabetically.

Step by Step Guide:

● Define a list using a variable num_strings and "hard code" the following four
  numerical strings: "15", "100", "55", "42".
● Define a list using a variable num_ints and hard code the following four
  numerical integers: 15, 100, 55, 42.
● Define a list using a variable num_floats and hard code any four floats you want.
● Define a list using a variable num_lists. This is going to be a lists of lists
  or a nested list!
  Use the following syntax: num_lists = [[1,2,3], [4,5,6], [7,8,9]]
● Print a summary of each variable (or list). The summary should contain:
    ○ A statement about the variable's type.
    ○ A statement about the elements of the variable.
    ○ A statement about the first element and its type.
    ○ Use formatting below.
● Permanently sort num_strings and num_ints.
● Print each list.
● Print a statement about what you discover when sorting these two lists.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output as below.

"""
print("Welcome to Types of Lists App")

# Defining the list
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [15.1, 100.2, 55.3, 42.4]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nSummary Table")
print(f"\nVariable num_strings is of type : {type(num_strings)}")
print(f"It contains the element : {num_strings}")
print(f"The element {num_strings[0]} is of type : {type(num_strings[0])}")

print(f"\nVariable num_ints is of type : {type(num_ints)}")
print(f"It contains the element : {num_ints}")
print(f"The element {num_ints[0]} is of type : {type(num_ints[0])}")

print(f"\nVariable num_floats is of type : {type(num_floats)}")
print(f"It contains the element : {num_floats}")
print(f"The element {num_floats[0]} is of type : {type(num_floats[0])}")

print(f"\nVariable num_lists is of type : {type(num_lists)}")
print(f"It contains the element : {num_lists}")
print(f"The element {num_lists[0]} is of type : {type(num_lists[0])}")

# Sorting the Lists
num_strings.sort()
num_ints.sort()

# Formatting the output
print("\nNow sorting num_strings and num_ints")
print(f"Sorted num_strings are : {num_strings}")
print(f"Sorted num_ints are : {num_ints}")
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")
