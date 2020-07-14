""" Description:

You are responsible for writing a program that sorts a list of comma separated
numbers as either even or odd. Upon sorting the numbers into two groups, your
program will then sort each group numerically and display the results.

Step by Step Guide:

● Print a welcome message.
● Create an active flag variable that will control a while loop and set it to True.
● Use this flag to run a while loop:
    ○ Get user input for a series of numbers separated by a comma.
        ■ This series of numbers will be a string, don’t change this for now.
        ■ Take precaution to remove any spaces the user may have put into the
number using the .replace() method for strings.
        ■ Replace “ “ a space with “” a blank string.
        ■ The user may enter "1, 2, 3, 4," or they may enter "1,2,3,4".
        ■ You want to have the results of the program be the same regardless.
    ○ Turn the string into a list using the .split() method for strings.
        ■ Each element in our list should be a number.
        ■ The string should be split using a comma.
        ■ For example, if i have a list values = [‘1,2,3,4,5’] calling values.split(“,”)
would return a list [‘1’, ‘2’, ‘3’, ‘4’, ‘5’].
    ■ Store this return value in a variable called num_list.
○ Create a blank list called evens.
○ Create a blank list called odds.
○ For every number in your list of numbers:
        ■ Cast the number to an integer.
        ■ Recall a number is even if it is divisible by 2.
        ■ If the number is even:
            ● Append the number to the evens lists.
            ● Print a statement that the number is even.
        ■ Else:
            ● Append the number to the odds lists.
            ● Print a statement that the number is odd.
    ○ Permanently sort your even numbers in numerical order.
    ○ Permanently sort your odd numbers in numerical order.
    ○ Display all the even numbers in numerical order as formatted below.
    ○ Display all odd numbers in numerical order as formatted below.
    ○ Get user input for if they would like to continue the program.
    ○ If the user does not want to continue:
        ■ Set your flag variable to False
        ■ Print a goodbye message thanking the user.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to Even Or Odd Number Sorter App")

running = True

# Run the program as long as user wants.
while running:
    number_string = input("\nEnter in a string of numbers separated by a comma (,) : ")
    number_string = number_string.replace(" ", "")
    number_list = number_string.split(",")

    # Initialize the list to hold even/odd values.
    evens = []
    odds = []

    # Calculate whether the number is even or odd.
    print("\nResult Summary\n")
    for number in number_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print(f"{number} is Even.")
        else:
            odds.append(number)
            print(f"{number} is Odd.")

    # Sort the lists evens and odds.
    evens.sort()
    odds.sort()

    # show the even numbers.
    print("\nThe following numbers are even : ")
    for even in evens:
        print(even)

    # show the odd numbers.
    print("\nThe following numbers are odd : ")
    for odd in odds:
        print(odd)

    # Ask the user whether they wish to continue or quit the program.
    choice = input("\nWould you like to continue (y/n) : ").lower()
    if choice != "y":
        running = False
        print("\nThank you for using Even Odd Number Sorter App. See You later.")
