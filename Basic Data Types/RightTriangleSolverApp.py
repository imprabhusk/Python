""" Description:

You are responsible for writing a program that will calculate the hypotenuse
and area of a right triangle given its two bases. Your program will round all
calculations to a precision of three decimal places and provide a summary of
the mathematical results.

Step by Step Guide:

● Print a welcome message.
● Get user input for the first side of the right triangle.
● Get user input for the second side of the right triangle.
● Calculate the hypotenuse of the right triangle using the Pythagorean theorem.
    ○ We can't actually take a square root with basic Python. In order to take
      a square root, we will need to import a library of extra code.
    ○ Type import math as the first line of code in your program.
    ○ This allows us to access higher level mathematical functions such as the
      square root function sqrt().
    ○ Google how to take a square root using the math library.
● Calculate the area of the right triangle.
● Round each value to 3 decimal places.
● Print a message to the user informing them of both the hypotenuse and area of
  the given triangle.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output as below.

"""
import math

print("Welcome to Right Triangle Solver App")

side_a = float(input("\nEnter the side 'a' of the triangle : "))
side_b = float(input("\nEnter the side 'b' of the triangle : "))

# calculate hypotenuse of the triangle
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)

# calculate area of the triangle
area = 0.5 * side_a * side_b

# format the output
print(f"\nHypotenuse for the sides {side_a} and {side_b} is {round(hypotenuse, 3)}")
print(f"\nArea of the Triangle for the {side_a} and {side_b} is {area}")
