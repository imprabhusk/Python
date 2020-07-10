""" Description:

You are responsible for writing a program that will simulate flipping a coin n
number of times. Your program will present the user an option to see the
result of each individual flip. Your program will also inform the user any
time the number of heads flipped is equal to the number of tails flipped. Upon
completion of all flips, your program will provide a summary table that shows
the number and percentage of each flip.

Step by Step Guide:

● Print a welcome message.
● Get user input for how many times the user would like to flip the coin.
● Get user input for whether they would like to see the result of each
  individual coin flip or not.
    ○ This response should be case insensitive.
    ○ Any response that starts with y should be taken as a yes.
● Create a variable to store the number of times heads is flipped and set it equal
  to zero.
● Create a variable to store the number of times tails is flipped and set it equal
  to zero.
● Flip a coin for the correct number of times.
● For each flip; do the following:
    ○ To simulate a coin flip we will randomly pick a number from two possible states.
        ■ The random generation of numbers is outside the scope of basic python. In
          order to generate random numbers we will need to import a library of
          extra code.
        ■ Type import random as the first line of code in your program.
    ○ Create a coin flip using the random library to generate a random integer; 0 or 1.
        ■ Let one of these values imply that a heads was flipped while the other
          implies that tails was flipped.
    ○ Use an if/else statement to increase the number of heads or tails flipped
      depending on the outcome of the coin flip.
    ○ If the user indicated that they want to see the individual results:
        ■ Display what was flipped.
    ○ If the number of heads and tails are equal:
        ■ Inform the user each time this occurred.
● Calculate the percentage of heads flipped.
● Calculate the percent of tails flipped.
● Round these values to two decimal places.
● Print out the results of the total trials as formatted below.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import random

print("Welcome to Coin Toss App")
print("\nI will flip a coin a set number of times")

flip_number = int(input("\nHow many times would you like to flip the coin : "))
choice = input("Would you like to see the result of each filp : ").lower()

print("\nFlipping\n")

# Initialize heads and tails variables
heads = 0
tails = 0

for flips in range(flip_number):
    coin = random.randint(0, 1)

    # create coin object
    if coin == 1:
        heads += 1
        if choice.startswith("y"):
            print("HEADS")
    else:
        tails += 1
        if choice.startswith("y"):
            print("TAILS")

    if heads == tails:
        print(
            f"At {flips + 1} flips, the number of heads and tails were equal at {heads}\
 each."
        )

# Calculate percentages
heads_percentage = round(100 * heads / flip_number, 2)
tails_percentage = round(100 * tails / flip_number, 2)

# print the result and format the output
print(f"\nResults of Flipping a Coin {flip_number} Times:")
print("\nSide\t\tCount\t\tPercentage")
print(f"Heads\t\t{heads} / {flip_number}\t\t{heads_percentage}%")
print(f"Tails\t\t{tails} / {flip_number}\t\t{tails_percentage}%")
