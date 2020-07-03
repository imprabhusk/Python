""" Description:

You are responsible for writing a program that will get a message and a
specific letter from a user and then count the number of occurrences of
that letter in the given message. You program should count “H” and “h” as
an occurence of h. Your program will then display a message to the user
stating the occurrences of the given letter.

"""

print("Welcome to the Letter Counter App")

name = input("\nWhat is your name : ").title().strip()
print("Hello", name.capitalize() + "!")

print(
    "\nI will count the number of times that a specific letter occurs in a \
message"
)

message = input("\nPlease Enter a Message : ")
letter = input("\nWhich letter would you like to count the occurence of : ")

message = message.lower()
letter = letter.lower()
letter_count = message.count(letter)
print(f"\n{name}, your message has {letter_count} {letter}'s in it.")
