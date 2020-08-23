""" Description :

You are responsible for writing a program that will roll a given number of
dice of any number of sides and sum the total. Your program will continue to
run until the user desires to quit.

Step by Step Guide:

Defining your functions:
● Define a function dice_sides() which takes zero parameters.
    ○ Get user input for how many sides their dice should have.
    ○ Return this value.
● Define a function dice_number() which takes zero parameters.
    ○ Get user input for how many dice they would like to roll.
    ○ Return this value.
● Define a function roll_dice() which takes in two parameters, the number of sides on the
  dice, and the number of dice to roll.
    ○ This function should simulate rolling the dice and store the values in a list.
    ○ Define a blank list called dice.
    ○ Print a message informing how many n sided dice the user rolled.
    ○ Roll the correct number of dice.
    ○ To roll a die, create a random integer from 1 up to the number of sides on the dice.
        ■ Type import random as the first line of code in your program.
    ○ Append this die value to your list.
    ○ When you have rolled all of the dice, return the list.
● Define a function sum_dice() which takes in one parameter, a list holding all the dice
  values.
    ○ This function should sum all the dice in the list.
    ○ Print the value of the sum.
    ○ There is no return value for this function.
● Define a function roll_again() which takes zero parameters.
    ○ Get user input for if they would like to roll again. ○ Thiscanbeayornvalue.
    ○ Return an appropriate Boolean (True or False) based on their response.
    ○ Use this return value to control a while loop running the app.
Your main code:
● Print a welcome message.
● Create an active flag variable and set it to True.
● Use this flag to control a while loop.
● Run your program to simulate a dice application. Your program should do the following:
    ○ Create the desired dice by calling the dice_sides() and dice_number() functions.
    ○ Roll the dice by calling the roll_dice() function.
    ○ Sum the dice by calling the sum_dice() function.
    ○ Ask the user if they would like to continue by calling the roll_again() function.
● When the user wants to stop the program print a goodbye message.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import random


def dice_sides():
    sides = int(input("\nHow many sides would you like on your dice: "))
    return sides


def dice_number():
    number = int(input("\nHow many dice would you like to roll : "))
    return number


def roll_dice(sides, number):
    dice = []
    print(f"\nYou rolled {number} {sides} sided dice.")
    print("\n..........Results are as followed..........")
    for i in range(number):
        value = random.randint(1, sides)
        print(f"\t\t{value}")
        dice.append(value)
    return dice


def sum_dice(dice):
    total = 0
    for die in dice:
        total += die
    print(f"The total value of your roll is {total}.")


def roll_again():
    choice = input("\nWould you like to roll again (y/n) : ")
    if choice != "y":
        roll = False
    else:
        roll = True
    return roll


print("Welcome to The Python Dice App")

rolling = True

while rolling:
    d_sides = dice_sides()
    d_number = dice_number()

    my_dice = roll_dice(d_sides, d_number)
    sum_dice(my_dice)

    rolling = roll_again()

print("\nThank you for using the Python Dice App.")
