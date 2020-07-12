""" Description:

You are responsible for writing a program that will conduct a poll on a yes or
no issue. Upon starting the program a user will be prompted for an issue to
vote on, the number of voters, and a password to view the poll results. You
program will then conduct the poll. Each time a user votes, your program will
ask for the voters full name to verify that they have not yet voted. If the
voter has not yet voted, they will be presented with the issue and can vote
yes or no. The vote will be recorded. Once the number of voters specified by
the user has been reached, the poll will close and a summary will be
displayed. If the user enters the correct password a result of each voters
name and how they voted will be displayed.


Step by Step Guide:

● Print a welcome message.
● Get user input for the issue that the voters will be voting on.
● Get user input for the number of voters that will be allowed to vote.
● Get user input for a password to be used to view the polling results.
● Define a variable to count the number of yes votes and initialize it to zero.
● Define a variable to count the number of no votes and initialize it to zero.
● Define a blank dictionary that will hold the results of the poll.
    ○ Each key in the dictionary will be a person's full name
    ○ The associated value will be their vote.
● Simulate the polling process by using a for loop the appropriate number of times.
● Each iteration of the loop:
    ○ Ask the user to enter their full name.
    ○ If the user's name has already been registered:
        ■ Print a message that informs them they cannot vote again.
    ○ Else, they haven't yet voted:
        ■ Print a message describing the issue that is to be voted on.
        ■  Get user input for their choice, yes or no.
            ● You should allow users to type 'yes', 'YES', 'Yes', 'y' or 'Y' for yes
              and similar for no.
            ● Depending on the user input, increment the number of yes or no votes by one.
            ● If they user entered in another option; record their vote but inform them
              that their vote was not yes or no and will not influence the poll.
        ■ Add a new element to your dictionary.
            ● The key of this element should be the user's name.
            ● The value of this element should be their choice; which regardless of how
              they entered it should be 'yes', 'no', or their invalid vote.
        ■ Print a message thanking the user and confirming their vote.
● Once the voting is finished, print a summary that shows the total number of voters.
● List the full names of all the voters.
● Give a final voting result.
● Reprint the issue that was being voted on.
● Use an if/elif/else chain to print an appropriate message if yes won, if no won, and if
  it was a tie.
● Get user input for a password to see the voting results, vote by vote.
● If the user enters the password correct:
    ○ Print all full names and their corresponding votes.
● Else:
    ○ Let the user know the password was not correct.
● Print a message thanking the user for using the program.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""
