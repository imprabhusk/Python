""" Description:

You are responsible for writing a program that will play the classic “Hi Low”
game. Your program will randomly pick a number between 1 and 20. Users will
then guess the number. With each guess, your program will respond that the
user’s guess is either too high or too low. When the user guesses correct, or
after 5 guesses, your program will end the game and summarize the results.

Step by Step Guide:

● Print a welcome message.
● Get user input for their name.
● Inform the user that you are thinking of a number between 1 and 20.
● Use the random library to generate a random integer between 1 and 20.
    ○ Type import random as the first line of code in your program.
● Allow the user to guess 5 times. Each time do the following:
    ○ Get the users guess.
    ○ If the guess is too low inform them.
    ○ Elif the guess is too high inform them.
    ○ Else the guess is the number use the​ ​break command to exit the for loop.
        ■ Google or reference the python documentation on how the break command works.
● If the user got the number correct, inform them and tell them how many guesses it took.
● If the user did not get the number correct after the 5th guess, let them know they lost.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import random

print("Welcome to Guess My Number App")

name = input("\nWhat is your name : ").title().strip()
print(f"\nHello {name}, I am thinking of a number between 1 and 20.")

# Pick a random integer from 1 to 20 using random module
number = random.randint(1, 20)

# Guess the number within 5 times
for guess_number in range(5):
    guess = int(input("\nTake your guess : "))

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too High.")
    else:
        break

# Format the output for winning and losing.
if guess == number:
    print(f"\nGood Job, {name}! You guessed my number in {guess_number + 1} guesses.")
else:
    print(f"\nGame Over. The number I was thinking is : {number}.")
