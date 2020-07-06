""" Description:

You are responsible for writing a program that will build and display a
basketball roster based off user input. Your program will then simulate an
injury to a specific player in the roster and prompt the user to update the
roster. Upon updating the roster, your program will display the final roster
and wish the newly add player good luck.


Step by Step Guide:

● Print a welcome message.
● Create a blank list called roster.
● Get user input for the names of the starting roster for a basketball team.
    ○ The starting roster includes a point guard, shooting guard, small forward, power
      forward, and center. Use an input statement for each position.
    ○ Make sure to always display the name capitalized.
    ○ Add each position to your list roster.
    ○ Your point guard should be index 0, shooting guard at index 1, ect...
● Print the starting 5 as formatted below.
● Remove the small forward from the list and store it in a variable called injured_player.
● Print a message to the user informing them that this player is injured.
● Get the length of the current roster.
● Print a message to the user informing them of the length of the current roster.
● Get user input for who will take the injured players spot and store this in a variable
  called added_player.
● Add this player to the roster at the correct position.
● Print the updated starting 5 as formatted below.
● Print a good luck message to the new player.
● Get the length of the current roster.
● Print a message to the user informing them of the length of the current roster.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to BasktetBall Roster App")

roster = []

# Get user input and define our roster
point_guard = input("\nWho is your point guard : ")
roster.append(point_guard)
shooting_guard = input("Who is your shooting guard : ")
roster.append(shooting_guard)
small_forward = input("Who is your small forward : ")
roster.append(small_forward)
power_forward = input("Who is your power forward : ")
roster.append(power_forward)
center = input("Who is your center : ")
roster.append(center)

# Display roster
print("\nYour starting five for the upcoming basketball season")
print(f"Point Guard\t\t : {roster[0]}")
print(f"Shooting Guard\t\t : {roster[1]}")
print(f"Small Forward\t\t : {roster[2]}")
print(f"Power Forward\t\t : {roster[3]}")
print(f"Center\t\t\t : {roster[4]}")

injured_player = roster.pop(2)

# Remove injured player
print(f"\nOh No!, {injured_player} is injured")
print(f"Your Roaster only has {len(roster)} player")

# Add new player
added_player = input(f"\nWho will take {injured_player} spot : ").title()
roster.insert(2, added_player)

# Display roster
print("\nYour starting five for the upcoming basketball season")
print(f"Point Guard\t\t : {roster[0]}")
print(f"Shooting Guard\t\t : {roster[1]}")
print(f"Small Forward\t\t : {roster[2]}")
print(f"Power Forward\t\t : {roster[3]}")
print(f"Center\t\t\t : {roster[4]}")

# Format output
print(f"\nGood Luck! {roster[2]}, You will do great!")
print(f"Your roster now has {len(roster)} players.")
