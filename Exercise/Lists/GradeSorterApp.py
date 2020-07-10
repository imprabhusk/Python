""" Description:

You are responsible for writing a program that will collect four grades from a
user. Your program will then sort these grades from highest to lowest. Then,
your program will simulate dropping the lowest two grades the user entered.
Lastly, it will comment on the users highest grade.

Step By Step Guide:

● Print a welcome message.
● Create a blank list called grades.
● Get user input to add 4 grades to the list.
    ○ Be aware of the data type you are using.
● Print the list as formatted below.
    ○ You may have to cast the list to a string.
● Permanently sort the list from highest to lowest.
● Inform the user that their lowest two grades are being dropped.
● Remove the lowest two grades from the list.
● Print a message informing the user that the grades were dropped.
● Print the remaining grades.
● Print the users highest grade with a message.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to Grade Sorter App")

# Initialize the list
grades = []

# Gather grades from the user
grade = int(input("\nWhat is your first grade (0 - 100) : "))

# Append grades to the list
grades.append(grade)
grade = int(input("What is your second grade (0 - 100) : "))
grades.append(grade)
grade = int(input("What is your third grade (0 - 100) : "))
grades.append(grade)
grade = int(input("What is your fourth grade (0 - 100) : "))
grades.append(grade)

# print all the grades entered by the user
print(f"\nYour grades are {grades}")

# Sort the list from highest to lowest
grades.sort(reverse=True)

print(f"\nYour Grades from highest to lowest : {grades}")

# Removing the lowest two grades
print("\nThe Lowest two grades will now be dropped")
removed_grade = grades.pop()
print(f"\nRemoved Grade is : {removed_grade}")
removed_grade = grades.pop()
print(f"\nRemoved Grade is : {removed_grade}")

# format the output
print(f"\nYour Remaining Grades are : {grades}")
print(f"\nCongratulations, Your Highest Grade is : {grades[0]}")
