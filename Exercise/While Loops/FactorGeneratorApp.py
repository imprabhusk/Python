""" Description:

You are responsible for writing a program that generates all factors of a
given number. Your program will display the factors individually and give a
mathematically summary of how different pairs of factors can be multiplied
together to get the given number.

Step by Step Guide:

● Print a welcome message.
● Create an active flag variable to control a while loop and set it to True.
● Use this flag to run a while loop:
    ○ Get user input for a number to determine the factors of.
    ○ Write an algorithm to determine the factors of the given number.
        ■ Create a blank list called factors.
        ■ Use a for loop to loop through the numbers 1 up to and including the
          given number:
● If the given number is divisible by the current number in the loop, the
  current number is a factor:
    ○ Add the current number to the list factors.
    ○ Modulo division will help you here.
    ○ Print all factors of the number as formatted below.
    ○ Print a summary which shows how the factors multiply together to get the
      users number using a for loop.
        ■ The first element in your list will pair with the last element.
            ● factors[0] and factors[-1]
        ■ The second element will pair with the second to last element.
            ● factors[1] and factors[-2]
        ■ The third element will pair with the third to last element.
            ● factors[2] and factors[-3]
        ■ Try to generalize this pattern using an iterable variable i.
        ■ You only need to loop through half of your list to accomplish this.
● for i in range(int(len(factors)/2))
    ○ Get user input for if they would like to continue the program.
    ○ If the user does not want to continue:
        ■ Set your flag variable to False
        ■ Print a goodbye message thanking the user.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import math

print("Welcome to the Factor Generator App")

running = True

# Run the program untill the user quits
while running:
    number = int(
        input("\nEnter a number to determine all the factors of that number : ")
    )

    # Find the factors for the given number
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    # Print out the factors
    print(f"\nFactors of {number} are : ")
    for factor in factors:
        print(factor)

    # Print a summary of the factors automatically
    print("\nIn Summary")
    for i in range(int(math.ceil(len(factors) / 2))):
        print(f"{factors[i]} * {factors[-i-1]} = {number}")

    # Ask the user if they would like to quit or continue
    choice = input("\nRun Again (y/n) : ").lower()
    if choice != "y":
        running = False
        print("\nThank you for using Factor Generator App. GoodBye!")
