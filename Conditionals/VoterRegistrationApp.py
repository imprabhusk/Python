""" Description:

You are responsible for writing a program that will simulate registering to
vote. If a user is 18 or older, your program will present them with a list of
potential political parties to register for. Upon choosing a party, your
program will confirm that the user has registered and print a specific message
depending on the party joined.

Step by Step Guide:

● Print a welcome message.
● Get user input for their name.
● Get user input for their age.
● Create the following list that holds the following political parties:
    ○ Republican, Democratic, Independent, Libertarian, Green]
● If the user is old enough to vote print a message informing the user they are
  old enough to vote.
    ○ List all the possible political parties to join as formatted below.
    ○ Get user input for the party they wish to join.
    ○ If the chosen party is in the list of voting parties print a message they
      have joined.
        ■ If the party is republican or democratic inform the user that it is a
          major party.
        ■ Elif the party is independent inform the user that they are an independent
          person.
        ■ Else inform the user that their party is not a major party.
    ○ Else inform the user that the party they chose is not a given party.
● Else inform the user they are not old enough to vote.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to Voter Registration App")

name = input("\nWhat is your name : ").title().strip()
age = int(input("What is your age : "))
parties = ["Republican", "Democratic", "Independent", "Libertian", "Green"]

if age >= 18:
    print(f"\nCongratulations {name}! You are eligible for voting.")
    print("\nHere is a list of political parties to join.")

    for party in parties:
        print("\t", party)

    chosen_party = input("\nWhat party would you like to vote : ").title().strip()

    if chosen_party in parties:
        print(f"\nCongratulations you have joined {chosen_party} party")
        if chosen_party == "Republican" or chosen_party == "Democratic":
            print("\nThat is major party!")
        elif chosen_party == "Independent":
            print(f"\nYou are an {chosen_party} person!")
        else:
            print("\nThat is not a major party.")

else:
    print("\nYou are not old enough to register for a vote")
