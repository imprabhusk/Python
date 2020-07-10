""" Description:

You are responsible for writing a program that will simulate playing the
classic game Rock, Paper, Scissors against computer AI. Your program will ask
the user how many rounds of the game they would like to play, simulate each
round, keep score, and determine an overall winner. Your program will also
print the classic phrases such as “Paper covers rock” or “Scissors cut paper”.

Step by Step Guide:

● Print a welcome message.
● Get user input for how many rounds they would like to play.
● Create a list called moves that holds three strings: 'rock', 'paper', and 'scissors'.
● Create a variable to hold the players score and set it to zero.
● Create a variable to hold the computer score and set it to zero.
● Play the game for the correct number of rounds using a for loop.
● Each round should do the following:
    ○ Print information for the current round.
        ■ This includes round number, player score, and computer score.
    ○ Have the computer randomly pick an element from the list moves.
        ■ Type import random as the first line of code in your program.
        ■ Randomly generate an integer from 0 to 2 which corresponds to an index
          in the list moves (0 = rock, 1 = paper, 2 = scissors).
        ■ Assign the computer a move based off this random index.
● Get the players choice of rock, paper, or scissors.
    ○ Make sure to make it case insensitive.
● If the player has made a valid move:
    ○ Print both moves.
    ○ Program the "logic" behind a game of rock, paper, scissors and play the round.
        ■ Rock beats scissors, scissors beats paper, paper beats rock.
        ■ For each outcome make sure you:
● Set a round winner (player or computer).
● Adjust the score.
● Set a phrase (rock smashes scissors!) to be displayed.
● Else the player has not made a valid move:
    ○ Let the computer win the round.
● After all rounds have been played, print out the final game statistics and print a
  statement indicating who won the game.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import random

print("Welcome to Rock, Paper and Scissor App")

name = input("\nWhat is your name : ").title().strip()
rounds = int(input(f"\n{name}, How many rounds would you like to play : "))

# Initialize the moves
moves = ["rock", "paper", "scissor"]

# Initialize the score for both player and computer
player_score = 0
computer_score = 0

# The main game loop
for game_rounds in range(rounds):
    # Each round details about player and computer
    print(f"\nRound {game_rounds} details:")
    print(f"Player Score\t\t : {player_score}")
    print(f"Computer Score\t\t : {computer_score}")

    # Let computer choose random integer from 0 to 2 using random module
    computer_index = random.randint(0, 2)
    computer_choice = moves[computer_index]
    player_choice = input(f"\nNow its your turn {name}: ").lower().strip()

    # If the player makes a valid move
    if player_choice in moves:
        print(f"\nComputer Choice : {computer_choice}")
        print(f"Player Choice : {player_choice}")

        # Computer chooses rock
        if player_choice == "rock" and computer_choice == "rock":
            winner = "Tie"
        elif player_choice == "paper" and computer_choice == "rock":
            winner = "Player"
        elif player_choice == "scissor" and computer_choice == "rock":
            winner = "Computer"

        # Computer chooses paper
        elif player_choice == "rock" and computer_choice == "paper":
            winner = "Computer"
        elif player_choice == "paper" and computer_choice == "paper":
            winner = "Tie"
        elif player_choice == "scissor" and computer_choice == "paper":
            winner = "Player"

        # Computer chooses scissors
        elif player_choice == "rock" and computer_choice == "scissor":
            winner = "Player"
        elif player_choice == "paper" and computer_choice == "scissor":
            winner = "Computer"
        elif player_choice == "scissor" and computer_choice == "scissor":
            winner = "Tie"

        # Catch for any other conditions
        else:
            print("\nRound winner not calculated")
            winner = "Tie"

        # Display round results
        if winner == "Player":
            print(f"\nYou won this round {game_rounds}.")
            player_score += 1
        elif winner == "Computer":
            print(f"\nComputer won this round {game_rounds}.")
            computer_score += 1
        else:
            print("\nThis round was a tie")

    # If the player makes invalid moves computer score's 1 point
    else:
        print("That is not a valid game option!")
        print("Computer gets the point")
        computer_score += 1

# Game Ended and Format the results
print("\nFinal Game Results:")
print("------------------------------")
print(f"Rounds played\t\t : {game_rounds}")
print(f"Player Score\t\t : {player_score}")
print(f"Computer Score\t\t : {computer_score}")
print("------------------------------")

# Announcing the winner of the game
if player_score > computer_score:
    print(f"\nCongratulations {name}, You won the match against Computer")
    print("You prooved that human brain is better than computer brain")
elif computer_score > player_score:
    print(f"\nComputer won this game against {name}")
else:
    print("\nThe game was a tie")
