""" Description:

You are responsible for writing a program that will get a message and a
specific letter from a user and then count the number of occurrences of
that letter in the given message. You program should count “H” and “h” as
an occurence of h. Your program will then display a message to the user
stating the occurrences of the given letter.

Step by Step Guide:

● Print a welcome message
● Get user input for their name.
    ○ Take proper precautions to always display the name capitalized.
● Print a message saying hello to the user using the user’s name.
● Print a message stating the goal of the program.
● Get user input for the message they would like to use.
● Get user input for the letter they would like to count.
    ○ Standardize both the message and letter such that “H” and “h” both
      count as an occurrence of the letter h.
● Create a variable called letter_count and set it equal to the
  number of occurrences of the given letter in the given message.
    ○ Use the .count() method.
● Print a message stating the number of occurrences of the given letter
  in the given message.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.
"""

print("Welcome to the Letter Counter App")

name = input("\nWhat is your name : ").title().strip()

print("\nHello", name.capitalize() + "!")

print("\nI will count the number of times that a specific letter occurs in a message")

message = input("\nPlease Enter a Message : ")

letter = input("\nWhich letter would you like to count the occurence of : ")

# Standardize to lower case
message = message.lower()
letter = letter.lower()

# Count the letter in a message
letter_count = message.count(letter)

# Format the output
print(f"\n{name}, your message has {letter_count} {letter}'s in it.")
