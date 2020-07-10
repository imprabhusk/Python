""" Description:

You are responsible for writing a program that will create a list of a user’s
favorite teachers. It will display these teachers ranked (assuming the first
teacher entered is the favorite, the second teacher entered is the next
favorite, ect...), alphabetically, in reverse alphabetical order, the top two
teachers, the next two teachers, the last favorite teacher, and the total
number of favorite teachers in the list. Your program will then add and remove
teachers from this list, each time displaying a similar summary.

Step By Step Guide:

● Print a welcome message.
● Create a blank list called fav_teachers.
● Prompt the user to enter in their four favorite teachers.
    ○ The user should only enter the last name of the teacher.
    ○ Make sure to title case all user input for sorting purposes.
● Add each of these teachers to the list fav_teachers.
● Print the favorite teachers ranked.
● Print the favorite teachers alphabetically.
● Print the favorite teachers in reverse alphabetical order.
● Print the top two teachers.
● Print the next two teachers.
● Print the last favorite teacher.
● Print the total number of favorite teachers.
● Follow the formatting below.

● Print a message to the user informing them that first favorite teacher is no longer
  their favorite teacher.
● Prompt the user to enter their new favorite teacher.
    ○ Store the name of this teacher in the first index of the list
    ○ Shift all other teachers down one index.
● Print the favorite teachers ranked.
● Print the favorite teachers alphabetically.
● Print the favorite teachers in reverse alphabetical order.
● Print the top two teachers.
● Print the next two teachers.
● Print the last favorite teacher.
● Print the total number of favorite teachers.
● Follow the formatting below.

● Print a message to the user informing them that they no longer like a teacher.
● Prompt the user to pick a teacher to remove from the list.
● Remove this teacher.
● Print the favorite teachers ranked.
● Print the favorite teachers alphabetically.
● Print the favorite teachers in reverse alphabetical order.
● Print the top two teachers.
● Print the next two teachers.
● Print the last favorite teacher.
● Print the total number of favorite teachers.
● Follow the formatting below.
● Use at least 2 comments to describe sections of your code
● “Chunk” your so that it is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to the Favorite Teacher App")

fav_teachers = []

# Get user input
fav_teachers.append(input("\nWho is your first favorite teacher : ").title())
fav_teachers.append(input("Who is your second favorite teacher : ").title())
fav_teachers.append(input("Who is your third favorite teacher : ").title())
fav_teachers.append(input("Who is your fourth favorite teacher : ").title())

# Summary of list
print(f"\nYour favorite teachers ranked are : {fav_teachers}")
print(f"Your favorite teachers alphabetically are : {sorted(fav_teachers)}")
print(
    f"Your favorite teachers in reverse alphabetical order are : \
{sorted(fav_teachers,reverse=True)}"
)

print(f"\nYour top two teachers are : {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two teachers are : {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your last favorite teacher is : {fav_teachers[-1]}")
print(f"You have total of {len(fav_teachers)} favorite teachers.")

# Insert a new favorite teacher
fav_teachers.insert(
    0,
    input(
        f"\nOops, {fav_teachers[0]} is no longer your favorite teacher. Who is your\
favorite teacher now : "
    ).title(),
)

# Summary of list
print(f"\nYour favorite teachers ranked are : {fav_teachers}")
print(f"Your favorite teachers alphabetically are : {sorted(fav_teachers)}")
print(
    f"Your favorite teachers in reverse alphabetical order are : \
{sorted(fav_teachers,reverse=True)}"
)

print(f"\nYour top two teachers are : {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two teachers are : {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your last favorite teacher is : {fav_teachers[-1]}")
print(f"You have total of {len(fav_teachers)} favorite teachers.")

# Remove a specific teacher
fav_teachers.remove(
    input(
        "\nYou've decided you no longer like a specific teacher. Which you like to remove\
 from the lists : "
    ).title()
)

# Summary of list
print(f"\nYour favorite teachers ranked are : {fav_teachers}")
print(f"Your favorite teachers alphabetically are : {sorted(fav_teachers)}")
print(
    f"Your favorite teachers in reverse alphabetical order are : \
{sorted(fav_teachers,reverse=True)}"
)

print(f"\nYour top two teachers are : {fav_teachers[0]} and {fav_teachers[1]}.")
print(f"Your next two teachers are : {fav_teachers[2]} and {fav_teachers[3]}.")
print(f"Your last favorite teacher is : {fav_teachers[-1]}")
print(f"You have total of {len(fav_teachers)} favorite teachers.")
