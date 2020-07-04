""" Description

You are responsible for writing a program that displays a multiplication table
and exponentiation table for any given number. Each table should show
mathematical results for operations performed with the given number and
integers from 1 to 9. The program will then print a series of messages to the
user describing how cool mathematics truly is.

Step By Step Guide:
● Print a welcome message.
● Get user input for their name.
● Get user input for their number.
● Define a variable called message that will hold the following string:
    ○ name.title() + ", Math is cool!"
● Create a multiplication table that calculates the product of the number entered
  and the numbers 1 through 9.
● Create an exponent table that calculates the exponential power of the number entered
  raised to the power 1 through 9.
● Each result should be rounded to 4 decimals.
● Each line in your table can be created in a single print statement.
    ○ I would recommend getting one line to work correctly.
    ○ Copy and paste the line the correct number of times, changing values accordingly
      for each subsequent line.
    ○ We will later learn a more efficient way to accomplish this task.
● Each table should have its own heading as below.
● Each mathematical result should be formatted as below.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output

"""

print("Welcome to Multiplication and Exponentiation App")

name = input("\nWhat is your name : ").title().strip()
print(f"\nHello {name.title()} Math is Cool! Let's Enjoy")

number = float(input("\nWhich number would you like to work with : "))

print(f"\nMultiplication Table for {number}")

print(f"\n{1.0} * {number} = {1.0 * number}")
print(f"{2.0} * {number} = {2.0 * number}")
print(f"{3.0} * {number} = {3.0 * number}")
print(f"{4.0} * {number} = {4.0 * number}")
print(f"{5.0} * {number} = {5.0 * number}")
print(f"{6.0} * {number} = {6.0 * number}")
print(f"{7.0} * {number} = {7.0 * number}")
print(f"{8.0} * {number} = {8.0 * number}")
print(f"{9.0} * {number} = {9.0 * number}")
print(f"{10.0} * {number} = {10.0 * number}")

print(f"\nExponentiation Table for {number}")

print(f"{number} ** {1} = {number ** 1}")
print(f"{number} ** {2} = {number ** 2}")
print(f"{number} ** {3} = {number ** 3}")
print(f"{number} ** {4} = {number ** 4}")
print(f"{number} ** {5} = {number ** 5}")
print(f"{number} ** {6} = {number ** 6}")
print(f"{number} ** {7} = {number ** 7}")
print(f"{number} ** {8} = {number ** 8}")
print(f"{number} ** {9} = {number ** 9}")
print(f"{number} ** {10} = {number ** 10}")
