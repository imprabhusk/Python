""" Description:

You are responsible for writing a program that will collect any number of
grades from a user. Your program will sort these grades numerically from
highest to lowest and calculate the grade point average of the user. Your
program will then ask for the average the user desires and calculate what the
user must get on their next assignment to achieve this average. Lastly, your
program will make a copy of the users grades and allow them to alter one of
their previous grades to see how doing worse or better on an assignment would
have changed their overall average.


Step By Step Guide:

● Print a welcome message.
● Get user input for their name.
● Get user input for the number of grades they would like to enter.
● Create an empty list that will hold the user's grades.
● Get user input for each individual grade and add it to the list.
● Sort the grades from highest to lowest and print each grade individually as
  formatted below.
● Calculate the average grade for the student as a float.
● Round this average to two decimal places.
● Display the students grade summary as formatted below.
    ○ This summary should include the user's name, the total number of grades,
      the highest grade,
      the lowest grade, and the average.
● Prompt the user for their desired average.
● Calculate what grade they need to get on their next assignment to achieve this
  average.
● Round this grade to two decimal places.
● Wish the user luck and inform them of the needed grade to get their desired average.
● Make a copy of your original list of grades.
● Get user input for a grade value that they would like to change.
● Get user input for the new grade value they would like the old grade changed to.
● Make the appropriate changes in the copy of the original list.
    ○ Please keep the original grades list in tact.
● Sort the new grades from highest to lowest and print each grade individually as
  formatted below.
● Calculate the new average grade for the student as a float.

"""

print("Welcome to Grade Point Average App")

# Get user input
name = input("\nWhat is your name : ").title().strip()
number_of_grades = int(input("\nHow many grades would you like to enter : "))

# Get the user's grades
grades = []
for grade in range(1, number_of_grades + 1):
    grades.append(int(input(f"Enter your grade {grade}: ")))

# Sort the grades and print them to the screen
grades.sort(reverse=True)
print(f"\nGrades from highest to lowest : {grades}")

# calculate the average
average = sum(grades) / len(grades)

# print user's grade summary
print(f"\n{name}'s Grade Summary : ")
print(f"\nTotal Number of Grades\t : {number_of_grades}")
print(f"Highest Grade\t\t : {max(grades)}")
print(f"Lowest Grade\t\t : {min(grades)}")
print(f"Average\t\t\t : {round(average, 2)}")

# Ask the user for their desired average to improve their grade in next assignments.
desired_average = float(input("\nWhat is your desired average : "))
required_grade = desired_average * (len(grades) + 1) - sum(grades)

# print summary
print(f"\nGood Luck, {name}!")
print(
    f"You will need to get a {round(required_grade, 2)} on your next assignment to earn a\
{desired_average} average."
)

# make a copy of the original grades and swap out one of them.
new_grades = grades[:]

print(
    "\nLet's see what you average could have been if you did better/worse on an\
assignment."
)
grade_change = int(input("What grade would you like to change : "))
new_grades.remove(grade_change)
new_grade = int(input(f"What grade would you like to change {grade_change} to : "))
new_grades.append(new_grade)

# sort the new grades
new_grades.sort(reverse=True)
print("\nNew Grades from highest to lowest : ")
for grade in new_grades:
    print(grade)

# calculate the new average
new_average = sum(new_grades) / len(new_grades)
print(f"\n{name}'s New Grade Summary : ")
print(f"\nTotal Number of Grades\t : {len(new_grades)}")
print(f"Highest Grade\t\t : {max(new_grades)}")
print(f"Lowest Grade\t\t : {min(new_grades)}")
print(f"New Average\t\t : {round(new_average, 2)}")
print(
    f"\nYour new average could be a {new_average} compared to your real average of \
{average}"
)

average_change = new_average - average

# print summary and format the output
print(f"That is a change of {round(average_change, 2)} points!")
print("\nToo Bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit!!!")
